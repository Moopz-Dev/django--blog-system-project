from django.db import models
from category.models import Category

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    writer = models.CharField(max_length=255)
    views = models.IntegerField(default=0)
    images = models.ImageField(upload_to="blogImages", blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
