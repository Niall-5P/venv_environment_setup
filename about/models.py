from django.db import models

class AboutPage(models.Model):
    """
    One-row table that stores content for /about/.
    If you want multiple pages later, just remove `unique=True`.
    """
    title       = models.CharField(max_length=100, default="About Aurarette")
    body        = models.TextField()
    hero_image  = models.ImageField(upload_to="about/", blank=True, null=True)
    updated_on  = models.DateTimeField(auto_now=True)

    # let Django use the plural “About page” in admin instead of “About pages”
    class Meta:
        verbose_name = "About page"

    def __str__(self):
        return self.title
