from django.db import models

from django.core.validators import MinValueValidator


    
# class Car(models.Model):
#    make = models.CharField(max_length=100, default='Unknown')
  
#    model = models.CharField(max_length=100)
#    manufacturing_year = models.PositiveIntegerField()
#    color = models.CharField(max_length=100, default='Unknown')
#    fuel_consumption = models.FloatField(default=0.0, validators=[MinValueValidator(0)])  # Default value specified with validator
#    car_type = models.CharField(max_length=20, default='Unknown')

#    price = models.FloatField()
#    image = models.CharField(max_length=2083)



class Car(models.Model):
    SEDAN = 'Sedan'
    JEEP = 'Jeep'
    HATCHBACK = 'Hatchback'
    CAR_TYPE_CHOICES = (
        (SEDAN, 'Sedan'),
        (JEEP, 'Jeep'),
        (HATCHBACK, 'Hatchback'),
    )

    make = models.CharField(max_length=100, null=True, blank=True)
    
    model = models.CharField(max_length=100,  null=True, blank=True)
    manufacturing_year = models.PositiveIntegerField(null=True, blank=True)
    color = models.CharField(max_length=100, default='Unknown')  # Default value specified
    fuel_consumption = models.FloatField(default=0.0, validators=[MinValueValidator(0)])
    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES, null=True, blank=True, default=SEDAN)  # Nullable field with default value specified
    price = models.FloatField( null=True, blank=True)
    image = models.CharField(max_length=2083)

    def __str__(self):
        return f"{self.make} {self.model} ({self.manufacturing_year})"


