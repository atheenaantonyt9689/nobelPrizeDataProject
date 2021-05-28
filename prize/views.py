from django.shortcuts import render
from django.views import View
from .models import Laureate
# Create your views here
#from django.views.generic import TemplateView

class HomePageView(View):
    model=Laureate
    template_name='core_section/home.html'
    def get(self,request,*args,**kwargs): 
        context={
            
        }
        
        return render(request,"core_section/home.html",context)
