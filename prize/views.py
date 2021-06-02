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
        
            
        data =NobelPrize.objects.values('category','laureate__born_country').annotate(Count('category'))
       
        print(data)
            
        
        context={
           "data":data

        }
        
        return render(request,"core_section/home.html",context)

class NobelPrizeGender(View):
    model=Laureate,NobelPrize
    template_name='core_section/gender_based_count.html'
    def get(self,request,*args,**kwargs):      
            
        gender_count =NobelPrize.objects.filter(year__range=["1990-01-01", "2000-01-31"]).values('category','laureate__gender','year','category').annotate(Count('year'))
        print(gender_count)

        context={
            "gender_count":gender_count
           

        }
        
        return render(request,"core_section/gender_based_count.html",context)

class AffiliationCount(View):
    count={}

    model=Laureate,NobelPrize
    template_name='core_section/gender_based_count.html'
    def get(self,request,*args,**kwargs): 
         
            
        affiliation_count =NobelPrize.objects.values('category','laureate__affiliation',).annotate(Count('laureate__affiliation'),Count('category')).order_by('-laureate__affiliation__count','-category')[:5]
        
        

        
        context={
            "affiliation_count":affiliation_count
           }
        
        return render(request,"core_section/count_affiliation.html",context)



