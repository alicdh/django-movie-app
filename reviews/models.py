from __future__ import unicode_literals

from django.db import models


class Movie(models.Model):
    movie_text = models.CharField(max_length = 20)
    movie_year = models.IntegerField(default = 0)
    def __str__(self):
        return self.movie_text
        
class Genre(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    genre_text = models.CharField(max_length=15, null=True)
    def __str__(self):
        return self.genre_text
        
class Actor(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    actor_text = models.CharField(max_length=35, null=True)
    def __str__(self):
        return self.actor_text
        
class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    rating_text = models.CharField(max_length=10)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.rating_text 
    
class Garbage(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    garbage_text = models.CharField(max_length=10)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.garbage_text 