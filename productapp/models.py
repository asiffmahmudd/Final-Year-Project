from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=500, null=True, blank=True)
    product_url = models.CharField(max_length=500, null=True, blank=True)
    product_price = models.IntegerField(null=True, blank=True)
    product_image = models.CharField(max_length=400, null=True, blank=True)
    vendor_name = models.CharField(max_length=20, null=True, blank=True)
    product_category = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.product_name