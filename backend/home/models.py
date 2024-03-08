from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    #used django hashing library
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"