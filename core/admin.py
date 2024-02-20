from django.contrib import admin

from .models import Action, ActionType, Order, PaymentOrder, Product, Rule

admin.site.register([Action, ActionType, Order, PaymentOrder, Product, Rule])
