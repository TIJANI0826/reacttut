from unicodedata import category
from django.db import models

# Create your models here.
class GroceryCategory(models.Model):
    category_name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.category_name

class Grocery(models.Model):
    category = models.ForeignKey(GroceryCategory,null=True,on_delete=models.SET_NULL)
    item_name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    
    
    
    def __str__():
        return self.item_name