from django.contrib.auth.models import User
from django.db import models


class SocialUser(models.Model):
    social_id = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Social ID'
    )
    token_id = models.TextField(
        blank=True,
        verbose_name='Token ID'
    )
    provider = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Provider'
    )
    auth_token = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Auth Token'
    )
    photo_url = models.URLField(verbose_name='Photo URL')
    user = models.OneToOneField(
        User,
        related_name='social_user',
        on_delete=models.CASCADE,
        verbose_name='User'
    )

    class Meta:
        verbose_name = 'Social User'
        verbose_name_plural = 'Social Users'
        unique_together = ('social_id', 'provider')

    def __str__(self):
        return f'{self.provider} {self.social_id}'
