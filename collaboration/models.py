from django.db import models


class CollaborationRequest(models.Model):
    full_name     = models.CharField(max_length=80)
    email         = models.EmailField()
    brand_name    = models.CharField(max_length=120, blank=True)
    website       = models.URLField(blank=True)
    message       = models.TextField()
    submitted_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.full_name} – {self.brand_name or 'Individual'}"
