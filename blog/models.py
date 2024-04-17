from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    author_image = models.ImageField(upload_to='authors/', blank=True, null=True)
    view_count = models.IntegerField(default=0)
    description = RichTextField()
    author = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    is_solved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    full_name = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()

    is_visible = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
from django.db import models

# Create your models here.
