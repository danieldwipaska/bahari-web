from typing import Any

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models


class CustomUserManager(UserManager):
    def create_user(self, email: str, password: str, **extra_fields: Any) -> "User":  # type: ignore
        """
        Creates and saves a User with the given email.
        """

        user: User = self.model(
            email=email,
            is_superuser=False,
            is_staff=False,
            is_blocked=False,
            is_active=True,  # type: ignore
            **extra_fields,
        )

        if password:
            user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields) -> "User":  # type: ignore
        user = self.create_user(email=email, password=password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_blocked = False
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField("Email Address", unique=True, blank=True, null=True)
    phone = models.CharField(max_length=30, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField("Staff Status", default=False)
    is_blocked = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return self.name or self.email or f"#{self.id}"
