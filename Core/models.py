from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

from django.db import models
# Create your models here.

class User(AbstractUser):
    # Add your additional fields here

    # Change the related_name for groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="custom_user_set",
        related_query_name="user",
        verbose_name=_('groups')
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="custom_user_set",
        related_query_name="user",
        verbose_name=_('user permissions'),
    )
