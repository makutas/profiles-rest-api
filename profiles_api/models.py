from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """This is manager for user profiles since we have modified the user model
    we need to tell django how to interact with it in order to create users.
    By default django expect the name but we added email"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        """Creates a new model that UserProfileManager is representing"""
        user.set_password(password)
        """We use here set_password function that comes with AbstractBaseUser - encryption
        pass is here converted into a hash and then stored in a db"""
        user.save(using=self._db)
        """Adding this line according to django docs"""
        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    """We need to use our custom user model with the Django CLI
    this is why django needs to have a custom model manager for the user model
    so it knows how to create users and control users using django command line tool"""

    USERNAME_FIELD = 'email'
    """Here we override the default username field (which is normally username)
    to be an email since we want the user to be identified by an email + password"""
    REQUIRED_FIELDS = ['name']
    """This is a required field for a user to specify / email is by default required"""

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a model as a string"""
        return self.status_text
