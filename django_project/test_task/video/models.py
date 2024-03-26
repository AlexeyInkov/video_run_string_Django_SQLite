from django.db import models


class VideoFile(models.Model):
    run_string = models.CharField(max_length=255)
    slug = models.SlugField()
    file = models.FileField()

