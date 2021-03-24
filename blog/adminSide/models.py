from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    class Meta:
        db_table = "categories"
    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(max_length=300, upload_to="posts")

    def __str__(self):
        return self.user.username

