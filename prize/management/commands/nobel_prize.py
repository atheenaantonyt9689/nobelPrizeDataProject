from django.core.management.base import BaseCommand
from django.db.models.fields import DateField
from prize.models import Laureate,NobelPrize
import requests
import json
class Command(BaseCommand):
    help = 'nobel_prize'

    def handle(self, *args, **kwargs):
        #url="https://api.nobelprize.org/v1/laureate.json "
        response=requests.get("https://api.nobelprize.org/v1/laureate.json").text
        response_info=json.loads(response)
        nobel_prizedata=response_info['laureates']

        for data in nobel_prizedata:

            prize_data=data['prizes']

            for prize in prize_data:
                #print(type(prize))
                affiliation_var=prize['affiliations']                 
                for aff_data in affiliation_var: 
                    #print(type(aff_data))
                             
                    obj1=NobelPrize.objects.create(year=prize['year'],category=prize['category'],share=prize['share'],motivation=prize['motivation'])
                    obj1.save()
                
                    obj2=Laureate.objects.create(nobel_prize=obj1,firstname=data['firstname'],surname=data['surname'],date_of_birth=data['born'],born_country=data['bornCountry'],gender=data['gender'],affiliation=aff_data['country'])
                    obj2.save()           
               
      
      
        

     