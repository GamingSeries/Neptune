from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

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

#-------------------------- Implementing Tables --------------------------#
# class UserLogin(models.Model):
#     email = models.EmailField(max_length=50, unique=True, blank=False)
#     password = models.CharField(max_length=128, blank=False)
    

#     class Meta:
#         verbose_name = 'User Login'
#         verbose_name_plural = 'User Logins'

#     def __str__(self):
#         return self.email  # Changed from self.username 

#     def save(self, *args, **kwargs):
#         self.password = make_password(self.password)
#         super().save(*args, **kwargs)

#     def check_password(self, raw_password):
#         return check_password(raw_password, self.password)