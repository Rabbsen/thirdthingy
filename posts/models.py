from django.db import models
from django.contrib.auth.models import User

# The post model here

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="fish_images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
