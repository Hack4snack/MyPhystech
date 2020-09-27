from django_use_email_as_username.models import BaseUser, BaseUserManager


# class User(BaseUser):
#     objects = BaseUserManager()

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


class ProfileManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


from django.db import models

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_mysql.models import ListCharField


class Profile(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    group_number = models.CharField(max_length=10)
    subscribe_channels = ListCharField(base_field=models.CharField(max_length=50), blank=True, max_length=500)
    subscribe_tags = ListCharField(base_field=models.CharField(max_length=50), blank=True, max_length=500)
    scheduled_channels = ListCharField(base_field=models.CharField(max_length=50), blank=True, max_length=500)
    scheduled_tags = ListCharField(base_field=models.CharField(max_length=50), blank=True, max_length=500)

    # @property
    # def subscribe_channels(self):
    #     return json.loads(self._subscribe_channels)
    #
    # @subscribe_channels.setter
    # def subscribe_channels(self, channel):
    #     self._subscribe_channels = json.dumps(channel)

    objects = ProfileManager()


from django.conf import settings
from django.contrib.sessions.models import Session


class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, null=True)
