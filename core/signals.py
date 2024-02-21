import json
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from logging import getLogger
from core.models import PaymentOrder
from core.utils import send_sqs_message


logger = getLogger(__name__)

@receiver(pre_save, sender=PaymentOrder)
def trigger_products_actions(sender, instance, **kwargs):
    try:
        # get the current version of the object
        current_status = sender.objects.get(id=instance.id).payment_status
    except sender.DoesNotExist:
        # if the object is being created, set current_status to None
        current_status = None
    if current_status != instance.payment_status and instance.payment_status == 'completed':
        for product in instance.order.products.all():
            rule = product.rules.first()
            if rule:
                for action in rule.actions.all():
                    # include product details on action message
                    action.configuration['product'] = {
                        'name': product.name,
                        'description': product.description,
                        'price': float(product.price),
                        'quantity': product.quantity,
                    }
                    # include order details on action message
                    action.configuration['order'] = {
                        'buyer_name': instance.order.user.get_full_name(),
                        'buyer_email': instance.order.user.email,
                        'payment_status': instance.payment_status,
                        'payment_method': instance.payment_method,
                    }
                    res = send_sqs_message(
                        slugify(action.action_type),
                        json.dumps(action.configuration),
                    )
                    logger.debug(res)
