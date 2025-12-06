from django.urls import path
from .views import ProfileView, ProfileListView

urlpatterns = [
    path('reservation/', ProfileView.as_view(), name='reservation_home'),
    path('profile/', ProfileListView.as_view(), name='reservation_list'),
]