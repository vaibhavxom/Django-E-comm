from django.db import models
from django.contrib.auth.models import User


class ShippingAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True ,blank= True)
    Shipping_full_name = models.CharField(max_length=255)
    Shipping_email = models.CharField(max_length=255)
    Shipping_address1 =models.CharField(max_length=255)
    Shipping_address2 =models.CharField(max_length=255)
    Shipping_city =models.CharField(max_length=255)
    Shipping_state =models.CharField(max_length=255, null= True ,blank= True)
    Shipping_zipcode =models.CharField(max_length=255, null= True ,blank= True)
    Shipping_country =models.CharField(max_length=255)

    #dont pluralise address
    class Meta :
        verbose_name_plural = "Shipping Address"

    def __str__(self) :
        return f'Shipping Address = {str(self.id)}'




