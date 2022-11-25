from django.conf.urls import url
from salary_data  import views

urlpatterns=[
    url(r'^salaryData$',views.salaryDataApi),
    url(r'^salaryData/([0-9]+)$',views.salaryDataApi),  
    url('salaryData',views.salaryDataApi),   #for search functionality
    
]