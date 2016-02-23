from django.db import models

class Token(models.Model):
    key = models.CharField(max_length=100)

    def __str__(self):
        return self.key
