from django.db import models

# Create your models here.


class Tool(models.Model):
    english_name = models.CharField(max_length=100, null=False, blank=False)
    english_description = models.CharField(max_length=200, null=False, blank=False)
    spanish_name = models.CharField(max_length=100, null=False, blank=False)
    spanish_description = models.CharField(max_length=200, null=False, blank=False)
    tool_image = models.CharField(max_length=50)
