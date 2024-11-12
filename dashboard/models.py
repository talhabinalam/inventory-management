from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


CHOICES = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Furniture', 'Furniture'),
    ('Medicine', 'Medicine')
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CHOICES)
    quantity = models.PositiveIntegerField(null=True, blank=True)

    # class Meta:
    #     verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name} + {self.category} - {self.quantity}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} - {self.staff} - {self.quantity}'

