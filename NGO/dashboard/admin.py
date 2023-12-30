from django.contrib import admin
from .models import Payments

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('pay_name', 'pay_mode', 'pay_amount', 'pay_trans_id')

admin.site.register(Payments, PaymentAdmin)
