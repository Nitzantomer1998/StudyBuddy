from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=20, unique=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name
    