from django.db import models

class menu(models.Model):
    item=models.CharField(max_length=20)
    cost=models.IntegerField()

  


