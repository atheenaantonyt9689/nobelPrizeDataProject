from django.db.models.aggregates import Count
from django.shortcuts import render
from django.views import View
from .models import Laureate, NobelPrize
# Create your views here
#from django.views.generic import TemplateView
from django.db.models import Sum

class HomePageView(View):
    model=Laureate,NobelPrize
    template_name='core_section/home.html'
    def get(self,request,*args,**kwargs): 
        
            
        data =NobelPrize.objects.values('category','laureate__born_country' ).annotate(Count('category'))
       
        print(data)
            
        
        context={
           "data":data

        }
        
        return render(request,"core_section/home.html",context)
