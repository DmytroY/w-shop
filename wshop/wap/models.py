from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wap:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    id = models.CharField(validators=[RegexValidator(r'^\d{12}$'),],max_length=12, primary_key=True)
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    image = models.ImageField(blank=True, null=True, default=None, upload_to='products')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    available = models.BooleanField(default=True)
    #available = models.IntegerField(null=False, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = ('id','slug')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wap:product_detail', args=[self.id, self.slug])



