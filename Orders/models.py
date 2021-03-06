from decimal import Decimal
from unicodedata import name

from django.conf import settings
from django.db import models
from Stores.models import Product
from .utils import PAYMENT_CHOICES

from pyuploadcare.dj.models import ImageField


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="order_user")
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    country_code = models.CharField(max_length=4, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)
    payment_option = models.ForeignKey('PayementMethode', on_delete=models.RESTRICT, related_name="payment_option", default='')
    id_trasaction = models.CharField(max_length=200, verbose_name="ID transaction")
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)


class PayementMethode(models.Model):
    name = models.CharField(choices=PAYMENT_CHOICES, max_length=150, unique=True)
    name_of_the_beneficiary = models.CharField(max_length=250, null=True)
    number_id = models.CharField(max_length=150, unique=True, null=True)
    # image = ImageField(blank=True, manual_crop="") 
    image = models.ImageField(upload_to="images/qr_code/", blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     if self.name in ('USDT (TETHER)', 'BITCOIN (BTC)', 'Tron (TRC20)'):
    #         print("yes 2")
    #         if not self.image:
    #             print("yes 3")
    #             from tempfile import TemporaryFile
    #             from django.core.files.storage import default_storage, Storage, DefaultStorage, FileSystemStorage
    #             from django.core.files.base import ContentFile
    #             from django.utils.encoding import force_str
    #             import qrcode
    #             from pyuploadcare import Uploadcare
    #             with TemporaryFile() as f:
    #                 print("yes 4")
    #                 img = qrcode.make(self.number_id)
    #                 img.save(f)
    #                 f.seek(0)
    #                 print("yes 5")
    #                 # print(f.read())
    #                 self.image = default_storage.save(force_str("%s.png"%self.name), ContentFile(f.read()))
                    
    #                 print("yes 2")
    #     super(PayementMethode, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)