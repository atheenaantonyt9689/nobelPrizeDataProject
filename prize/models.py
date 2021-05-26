from django.db import models

class Laureate(models.Model):
    firt_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth=models.DateField()
    born_country=models.CharField(max_length=100)
    affiliation=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    nobel_prize=models.ForeignKey('NobelPrize',on_delete=models.CASCADE,blank=True,
        null=True)
    def __str__(self):
        return self.firt_name
   
   

class NobelPrize(models.Model):
    year= models.CharField(max_length=100)
    category= models.CharField(max_length=100)
    share =models.CharField(max_length=100)
    motivation =models.CharField(max_length=100)


    def __str__(self):
        return self.category