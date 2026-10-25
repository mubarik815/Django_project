
from django.conf import settings
from django.db import models
from django.utils import timezone


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_day = models.CharField(max_length=10, null=True, blank=True, editable=False)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notes"
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_day = timezone.localtime(
                timezone.now()
            ).strftime("%A")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

