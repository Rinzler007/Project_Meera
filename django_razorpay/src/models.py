from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
class Corals(models.Model):
    name=models.CharField(max_length=100)
    email= models.EmailField(verbose_name='Email Address', unique=True, null=False, blank=False)
    contact_no= PhoneNumberField(verbose_name='Contact No.', blank=False, null=False, help_text='Add country code before the contact no.')
    address_1 = models.CharField(verbose_name='Address 1', max_length = 100, blank = False)
    address_2 = models.CharField(verbose_name='Address 2', max_length = 100, blank = False)
    pincode = models.CharField(verbose_name='Pincode', max_length = 6, blank = False)
    city = models.CharField(verbose_name='City', max_length = 100, blank = False)
    state = models.CharField(verbose_name='State', max_length = 100, blank = False)
    country = models.CharField(verbose_name='Country', max_length = 100, blank = False)
    package=models.IntegerField(verbose_name='Package No.', null=True, blank=False)
    type = models.CharField(verbose_name='Type', null=True, max_length = 100, blank = True)
    set = models.CharField(verbose_name='Set', null=True, max_length = 100, blank = True)
    amount=models.IntegerField(verbose_name='Amount', null=True, blank=True)
    order_id=models.CharField(max_length=100, blank=True)
    razorpay_payment_id=models.CharField(max_length=100, blank=True)
    paid=models.BooleanField(default=False)