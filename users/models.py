from django.db import models


class Base(models.Model):
    """
    Abstract base model with common fields for other models.
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    is_active = models.BooleanField(default=True, verbose_name="Is Active?")

    class Meta:
        ordering = ['-created_at']  # Default ordering

    def __str__(self):
        return f"Base Model - {self.id}"

    def soft_delete(self):
        """Soft delete instead of actual deletion."""
        self.is_active = False
        self.save()