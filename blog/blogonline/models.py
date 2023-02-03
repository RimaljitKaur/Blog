from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200,unique=True)
    published_on = models.DateField(auto_now=False)
    description = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=300, null=True)
    content = models.TextField()
    tags = TaggableManager()

    # def get_year(self):
    #     return self.published_on.year

    #def __str__(self) -> str:
     #   return self.title