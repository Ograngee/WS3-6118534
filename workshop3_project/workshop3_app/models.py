from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Attend(models.Model):
    ATTN_Number = models.IntegerField()
    Movie_Name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    show_time = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.Movie_Name} - {self.ATTN_Number}"
