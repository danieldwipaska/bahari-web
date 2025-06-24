from django.db import models


class LiveMusic(models.Model):
    name = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to="live_music/photos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Live Music"
        verbose_name_plural = "Live Music"
        ordering = ["name"]

    def __str__(self):
        return self.name
