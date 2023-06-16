from django.contrib import admin
from .models import WebsiteSetting, UserProfile, MetaInfo, UserLogin
# Register your models here.

admin.site.register(WebsiteSetting)
admin.site.register(UserProfile)
admin.site.register(MetaInfo)
admin.site.register(UserLogin)