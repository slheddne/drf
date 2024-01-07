# Imports -> Django
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Model -> Song model to represent the Song model
class Song(models.Model):
    title = models.CharField(max_length=50)
    duration = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(15)])
    release_year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2024)])

    # Method -> String representation of the model
    def __str__(self):
        return self.title
