from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
import random
import string
from datetime import timedelta
from django.utils import timezone

class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # 🔹 Fix
        blank=True
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # 🔹 Fix
        blank=True
    )

    def __str__(self):
        return self.username


User = get_user_model()

class PasswordResetOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reset_otps")
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def generate_otp(self):
        """Generate a 6-digit OTP"""
        otp = ''.join(random.choices(string.digits, k=6))
        return otp

    def is_expired(self):
        """Check if the OTP has expired"""
        return timezone.now() > self.expires_at

    def save(self, *args, **kwargs):
        # Set expiry time for OTP (e.g., 10 minutes)
        self.expires_at = timezone.now() + timedelta(minutes=10)
        if not self.otp:
            self.otp = self.generate_otp()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"OTP for {self.user.email} valid till {self.expires_at}"