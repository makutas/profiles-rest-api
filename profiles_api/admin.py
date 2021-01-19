from django.contrib import admin
from profiles_api import models

admin.site.register(models.UserProfile)
"""This tels the django admin to register UserProfile model with the admin site"""
admin.site.register(models.ProfileFeedItem)
