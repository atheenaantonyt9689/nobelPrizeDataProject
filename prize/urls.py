from django.urls import path
from .views import HomePageView,NobelPrizeGender,AffiliationCount
urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('gender_count', NobelPrizeGender.as_view(), name='gender'),
path('affiliation_count', AffiliationCount.as_view(), name='affiliation')
]
