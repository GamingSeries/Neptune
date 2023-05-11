from django.contrib import admin
from .models import WebsiteSetting, UserProfile, MetaInfo
# Register your models here.

admin.site.register(WebsiteSetting)
admin.site.register(UserProfile)
admin.site.register(MetaInfo)