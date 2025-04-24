from django.db import models


class FAQ(models.Model):
    """Frequently Asked Question"""
    question = models.CharField(max_length=200)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0,
                                        help_text="Lower numbers appear first")

    class Meta:
        ordering = ["order"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question[:50]
