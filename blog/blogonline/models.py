from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200,unique=True)
    published_on = models.DateField(auto_now=True)
    description = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(unique=True, max_length=300)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title