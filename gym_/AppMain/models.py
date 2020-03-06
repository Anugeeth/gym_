from django.db import models

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    address = models.CharField(max_length=500)
    join_date = models.DateField(("Date Joined"), auto_now=False, auto_now_add=False)
    photo = models.CharField(("Photo"), max_length=200)

    def __str__(self):
        return self.name
    
