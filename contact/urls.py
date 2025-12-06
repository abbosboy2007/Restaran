from django.urls import path
from .views import ContactView 

urlpatterns = [
    # path('', ContactView.as_view(), name='create_contact'),
    path('contact/', ContactView.as_view(), name='create_contact'),
    
]