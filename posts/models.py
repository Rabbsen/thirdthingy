from django.db import models
from django.contrib.auth.models import User

# The post model here

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    length = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="fish_images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# admin delete posts also deletes associated image files

import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Post)
def delete_associated_image(sender, instance, **kwargs):
    try:
        
        if instance.image:
            instance.image.delete(save=False)
    
    except Exception:
        pass
