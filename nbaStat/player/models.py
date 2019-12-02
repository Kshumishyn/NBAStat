from django.db import models
# Create your models here.


class player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    pid = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['id', 'full_name']

    def __str__(self):
        return "{} ".format(self.id) + self.full_name
