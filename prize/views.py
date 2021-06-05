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
            
        #data =NobelPrize.objects.values('laureate__born_country',)#.annotate(Count('category').filter('category[physics]'))
        ss=NobelPrize.objects.values('laureate__born_country','category').annotate(Count('category'))
       
        print(ss)
            
    
        context={
          #"data":data
          "ss":ss

        }
        
        return render(request,"core_section/home.html",context)

class NobelPrizeGender(View):
    model=Laureate,NobelPrize
    template_name='core_section/gender_based_count.html'
    def get(self,request,*args,**kwargs):      
            
        gender_count1 =NobelPrize.objects.filter(year__range=["1990-01-01", "2000-01-1"]).values('laureate__gender',).annotate(Count('id'))
        gender_count2 =NobelPrize.objects.filter(year__range=["2000-01-01", "2020-01-31"]).values('laureate__gender').annotate(Count('id'))

        print("first:",gender_count1)
        print("second:",gender_count2)

        context={
            "gender_count1":gender_count1,
             "gender_count2":gender_count2
           
        }
        
        return render(request,"core_section/gender_based_count.html",context)

class AffiliationCount(View):
    model=Laureate,NobelPrize
    template_name='core_section/count_affiliation.html'
    def get(self,request,*args,**kwargs):            
        affiliation_count =NobelPrize.objects.values('laureate__affiliation',).annotate(Count('id')).order_by('-id__count')[:5]
               
        print(affiliation_count)
        

        
        context={
            "affiliation_count":affiliation_count
           }
        
        return render(request,"core_section/count_affiliation.html",context)



