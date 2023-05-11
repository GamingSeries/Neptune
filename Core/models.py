from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class WebsiteSetting(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Website Setting'
        verbose_name_plural = 'Website Settings'

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/')

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.username

class MetaInfo(models.Model):
    page_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    keywords = models.TextField()

    class Meta:
        verbose_name = 'Meta Info'
        verbose_name_plural = 'Meta Infos'
    def __str__(self):
        return self.page_name