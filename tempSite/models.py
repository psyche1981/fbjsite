from django.db import models

# Create your models here.

class League(models.Model):
	league_id = models.AutoField(primary_key=True)
	league_name = models.CharField(max_length=100)
	country = models.CharField(max_length=50)
	active = models.BooleanField(default=False)	

	def __str__(self):
		return self.league_name

class Team(models.Model):
	team_name = models.CharField(max_length=100, primary_key=True)
	league = models.ForeignKey('League', on_delete=models.SET_DEFAULT, default=0)

	def __str__(self):
		return self.team_name

class Player(models.Model):
	player_id = models.AutoField(primary_key = True)
	player_name = models.CharField(max_length=100)
	active = models.BooleanField(default=False)

	def __str__(self):
		return self.player_name
