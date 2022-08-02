from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Product(models.Model):
    code = models.CharField(validators=[RegexValidator(r'^\d{12}$'),],max_length=12, primary_key=True)
    name = models.CharField(max_length=20)
    product = models.CharField(max_length=50)
    productivity = models.CharField(max_length=50)
    shortDescr = models.CharField(max_length=100)
    longDescr = models.TextField()
    price = models.FloatField(null=False, default=0)
    available = models.IntegerField(null=False, default=0)
    blocked = models.IntegerField(null=False, default=0)
    w_d_h = models.CharField(max_length=14)
    w_d_h_packed = models.CharField(max_length=14)
    weight = models.FloatField(null=False, default=0)
    weight_packed = models.FloatField(null=False, default=0)
    photo = models.ImageField(blank=True, null=True, default=None, upload_to='products')

    def save(self, *args, **kwargs):
        self.price = round(self.price, 2)
        print(f"====== self.price = {self.price}")
        super(Product, self).save(*args, **kwargs)

    def __repr__(self):
        return f'{self.code}, {self.name}, {self.product} '



