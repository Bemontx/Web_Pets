from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    phone_numer = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        texto = '{0} {1} {2} {3} {4}'
        return texto.format(self.name,self.last_name,self.age,self.phone_numer,self.email)
    
    class Meta:
        db_table = 'User'
        
class Pets(models.Model):
    name = models.CharField(max_length=150)
    race = models.CharField(max_length=150)
    age = models.IntegerField()
    
    def __str__(self):
        texto = '{0} {1} {2}'
        return texto.format(self.name,self.race,self.age)
    
    class Meta:
        db_table = 'Pet'
