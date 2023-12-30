from django.db import models

class Payments(models.Model):
    pay_name = models.CharField(max_length=300,default="Anonymous", blank=True)
    pay_mode = models.CharField(max_length=100, blank=True)
    pay_amount = models.CharField(max_length=100, blank=True)
    pay_trans_id = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.pay_name


