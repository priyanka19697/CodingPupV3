from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('auth.User', related_name='blogs', on_delete=models.CASCADE)
    # categories = models.ManyToManyField('Category')
    # featured_image = models.ImageField(upload_to='blog_images', blank=True, null=True)
    # slug = models.SlugField(unique=True)
    # views_count = models.PositiveIntegerField(default=0)
    # likes_count = models.PositiveIntegerField(default=0)
    # comments = models.ManyToManyField('Comment')
    # STATUS_CHOICES = [
    #     ('draft', 'Draft'),
    #     ('published', 'Published'),
    #     ('archived', 'Archived'),
    # ]
    # status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    # meta_description = models.CharField(max_length=200, blank=True)
    # meta_keywords = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title
    

#  extended functionality

# class Category(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name


# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Comment by {self.user.username}'
