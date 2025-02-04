from django.db import models
from django.contrib.auth.models import User

class Mentor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expertise = models.JSONField()
    availability = models.JSONField()
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.expertise}'
