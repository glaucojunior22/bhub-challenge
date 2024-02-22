from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Action, ActionType, Order, PaymentOrder, Product, Rule

class TestModels(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.product = Product.objects.create(name='Book', price=19.99)
        self.order = Order.objects.create(user=self.user, total_price=24.98)
        self.order.products.add(self.product)
        self.payment_order = PaymentOrder.objects.create(
            order=self.order,
            payment_status='pending',
            payment_method='card',
        )
        self.action_type = ActionType.objects.create(name='HTTP')
        self.action = Action.objects.create(
            name='Test for HTTP',
            action_type=self.action_type,
            configuration={}
        )
        self.rule = Rule.objects.create(
            name='Test Rule',
            product=self.product,
        )
        self.rule.actions.add(self.action)
    
    # Product
    def test_product_str_representation(self):
        self.assertEqual(str(self.product), 'Book')
    
    def test_product_price(self):
        self.assertEqual(self.product.price, 19.99)

    def test_product_default_quantity(self):
        self.assertEqual(self.product.quantity, 1)

    # Order
    def test_order_total_price(self):
        self.assertEqual(self.order.total_price, 24.98)
    
    def test_order_buyer(self):
        self.assertEqual(self.order.user, self.user)
    
    def test_order_products(self):
        self.assertEqual(self.order.products.count(), 1)
    
    # PaymentOrder
    def test_payment_order_order(self):
        self.assertEqual(self.payment_order.order, self.order)
    
    def test_payment_order_payment_status(self):
        self.assertEqual(self.payment_order.payment_status, 'pending')
    
    def test_payment_order_payment_method(self):
        self.assertEqual(self.payment_order.payment_method, 'card')

    # ActionType
    def test_action_type_str_representation(self):
        self.assertEqual(str(self.action_type), 'HTTP')
    
    # Action
    def test_action_str_representation(self):
        self.assertEqual(str(self.action), 'Test for HTTP')
    
    def test_action_type(self):
        self.assertEqual(self.action.action_type, self.action_type)
    
    def test_action_configuration(self):
        self.assertEqual(self.action.configuration, {})
    
    # Rule
    def test_rule_str_representation(self):
        self.assertEqual(str(self.rule), 'Test Rule')
    
    def test_rule_action(self):
        self.assertEqual(self.rule.actions.count(), 1)
    
    def test_rule_product(self):
        self.assertEqual(self.rule.product, self.product)
