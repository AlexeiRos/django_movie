from django.db import models


class Contact(models.Model):
    """Подписка по email"""
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name