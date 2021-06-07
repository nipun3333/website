from django.db import models

# Create your models here.
class Categories(models.Model):
    category = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.category

class Products(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    desc = models.TextField()
    
    def __str__(self):
        return self.title