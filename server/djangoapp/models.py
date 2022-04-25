from django.db import models
from django.utils.timezone import now
from django.core import serializers 
import uuid

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(max_length=1000)
    id = models.IntegerField(default=1, primary_key=True)
    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description

class CarModel(models.Model):
    SEDAN = 'Sedan'
    TRUCK = "Truck"
    SPORTS_CAR = "Sports car"
    CONVERTIBLE = "Convertible"
    COUPE = "Coupe"
    HATCHBACK = "Hatchback"
    SUV = 'SUV'
    WAGON = 'WAGON'
    CHOICES = [
        (SEDAN, 'Sedan'),
        (TRUCK, 'Truck'),
        (COUPE, "Coupe"),
        (HATCHBACK, "Hatchback"),
        (SPORTS_CAR, "Sports car"),
        (CONVERTIBLE, "Convertible"),
        (SUV, 'SUV'),
        (WAGON, 'WAGON')
    ]
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    id = models.IntegerField(default=1, primary_key=True)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=CHOICES)
    year = models.DateField(default=now)

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Type: " + self.type
# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership, name, purchase, review):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        #optional
        self.purchase_date = ""
        self.car_make = ""
        self.car_model = ""
        self.car_year = ""
        self.sentiment = ""
        self.id = ""

    def __str__(self):
        return "Dealer name: " + self.name