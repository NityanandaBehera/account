from django.urls import path,include
from .views import*

urlpatterns = [
    path('', show_product,name='show_product'),
    path('pdf_report/', pdf_report,name='pdf_report'),
]