from django.db import models

# Create your models here.
class Tour(models.Model):
    id = models.AutoField(primary_key=True)
    origin_country = models.CharField(max_length=250)
    destination_country = models.CharField(max_length=250)
    number_of_days = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_nights = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}, {self.number_of_days} days {self.origin_country} to {self.destination_country}"

