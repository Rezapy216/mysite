from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_views = models.IntegerField(default=0)  # (default=0)
    status = models.BooleanField(default=False)
    published_time = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    images = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.id}, {self.title}'

    def snippets(self):
        return self.content[:100] + '...'


