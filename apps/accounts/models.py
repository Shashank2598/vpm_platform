from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomManager(UserManager):

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superUser and sets is_staff and is_superuser true and then
        creates a user with the given email and password
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password, **extra_fields):
        """`
        Creates and saves a BaseUser with the given email and password.
        """

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class BaseUser(AbstractUser):
    """
        Model for user model with fields:
        email= required  and uniques field
        password= stores a hashed password
        first_name and last_name fields= not required
    """
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomManager()
