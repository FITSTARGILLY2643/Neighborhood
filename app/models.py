from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length = 50)
    location = models.ForeignKey('Location',on_delete = models.CASCADE,null = True)
    admin = models.ForeignKey(User,on_delete = models.CASCADE)
    occupants = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def create_neighborhood(self):
        self.save()
        
    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,neigborhood_id):
        neighborhood = cls.objects.get(id = neigborhood_id)
        return neighborhood