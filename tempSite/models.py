from django.db import models

# Create your models here.

class League(models.Model):
	league_id = models.AutoField(primary_key=True)
	league_name = models.CharField(max_length=100)
	country = models.CharField(max_length=50)
	active = models.BooleanField(default=False)	

	def __str__(self):
		return self.league_name
