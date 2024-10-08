from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts")
)

STATUS = (
    (0, "Unavailable"),
    (1, "available")
)

class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(default=timezone.now)  # Use timezone.now instead of True
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='meal_images/', null=True, blank=True)  # New image field

    def __str__(self):
        return self.meal
