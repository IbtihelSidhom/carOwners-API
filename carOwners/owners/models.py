from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200)
    car_model_year = models.IntegerField()
    car_vin = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    class Meta:
        db_table = 'owners'

    def __str__(self):
        return self.first_name