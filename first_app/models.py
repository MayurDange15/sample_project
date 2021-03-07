from django.db import models

# Create your models here.
class Seq(models.Model):
    sample_id= models.CharField(max_length=10, unique=True)
    sample_seq= models.TextField(max_length=200)

    def __str__(self):
        return self.sample_id
