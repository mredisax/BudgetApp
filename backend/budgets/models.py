from django.db import models

# Create your models here.
class Budget(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_budget')
        ]