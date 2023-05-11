from django.db import models

# Create your models here.

class WebsiteSetting(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return self.user.username

class MetaInfo(models.Model):
    page_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    keywords = models.TextField()

    def __str__(self):
        return self.page_name