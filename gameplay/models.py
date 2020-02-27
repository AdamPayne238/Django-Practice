# -*- coding: utf-8 -*-

from django.db import models
# Create your models here.

from django.db import models


class Game(models.Model):
    first_player = models.ForeignKey(User,  # Foreign Key to User Model (django comes w/ default User class)
                                     related_name="games_first_player")
    second_player = models.ForeignKey(User,
                                    related_name="games_second_player")

    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now_add=True

class Move(models.Model):
    x = models.IntegerField()  # Coordinates where move was made
    x = models.IntegerField()  # Coordinates where move was made
    comment = models.CharField(max_length=300, blank=True)  # Player can make comment w/ every move
    by_first_player = models.BooleanField()  # Determines who made the move


        game=models.ForeignKey(Game, on_delete=models.CASCADE())  # If game gets deleted so do all the moves connected