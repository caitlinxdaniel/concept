from django.db import models

# Create your models here.
class Phrase(models.Model):
    name = models.CharField(max_length=200, unique=True)
    difficulty = models.CharField(max_length=20)
    category = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

class Concept(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    icon = models.FileField(upload_to='icons/', blank=True, null=True)

    def __str__(self):
        return self.name

class Token(models.Model):
    COLOR_CHOICES = (
        ('green', 'Green'),
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        ('black', 'Black')
    )
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='green')
    concept = models.ForeignKey(Concept, on_delete=models.SET_NULL, blank=True, null=True)
    is_primary = models.BooleanField(default=False)
