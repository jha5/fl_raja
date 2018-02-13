from django.db import models
from django_extensions.db.models import TimeStampedModel
# Create your models here.
class Position(TimeStampedModel):
	id = models.AutoField(primary_key = True)
	lng = models.FloatField(null=False,blank=False,max_length=50)
	lat = models.FloatField(null=False,blank=False,max_length=50)
	def __str__(self):
		return str(self.id)

class City(TimeStampedModel):
	id = models.AutoField(primary_key = True)
	city_name = models.CharField(null=False,blank=False,max_length=25)
	pos = models.ForeignKey(Position)
	
	def __str__(self):
		return str(self.city_name)