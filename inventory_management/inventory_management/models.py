from django.db import models
from django.core.validators import RegexValidator

class ClothingItem(models.Model):
    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

    COLOR_CHOICES = [
        ('White', 'White'),
        ('Black', 'Black'),
        ('Gray', 'Gray'),
        ('Beige', 'Beige'),
        ('Cream', 'Cream'),
        ('Navy', 'Navy'),
        ('Brown', 'Brown'),
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Yellow', 'Yellow'),
        ('Green', 'Green'),
        ('Orange', 'Orange'),
        ('Purple', 'Purple'),
        ('Olive', 'Olive'),
        ('Burgundy', 'Burgundy'),
        ('Pink', 'Pink'),
        ('Sky Blue', 'Sky Blue'),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField(verbose_name="Price")

    def __str__(self):
        return f"{self.name} ({self.size}, {self.color})"
