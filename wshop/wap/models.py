from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class Stock(models.Model):
    code = models.IntegerField(validators=[MinLengthValidator(12), MaxLengthValidator(12)], primary_key=True)
    description = models.CharField(max_length=80)
    plant = models.CharField(max_length=4)
    location = models.CharField(max_length=4)
    unrestricted = models.IntegerField()
    valueUnrestricted = models.IntegerField()
    blocked = models.IntegerField()

    price = models.FloatField()
    photo = models.ImageField(blank=True, null=True, default=None, upload_to='products')

    def __repr__(selfself):
        return(f'{code} {description} {unrestricted} {price}')

