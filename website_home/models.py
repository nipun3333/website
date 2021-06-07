from django.db import models

# Create your models here.
class Categories(models.Model):
    category = models.CharField(max_length=100, blank=False)
    cat_desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category
    
class Images(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False, default='logo.png')

class Products(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False, default='logo.png')
    desc = models.TextField()
    
    def __str__(self):
        return self.title