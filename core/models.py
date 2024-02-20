from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order {self.id}'


class PaymentOrder(models.Model):
    PAYMENT_METHODS = (
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
    )
    PAYMENT_STATUSES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHODS)
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUSES)

    def __str__(self):
        return f'Payment for {self.order}'


class ActionType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Action(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    action_type = models.ForeignKey(ActionType, on_delete=models.CASCADE)
    configuration = models.JSONField()

    def __str__(self):
        return self.name


class Rule(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    actions = models.ManyToManyField(Action)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='rules',
        related_query_name='rule',
    )

    def __str__(self):
        return self.name
