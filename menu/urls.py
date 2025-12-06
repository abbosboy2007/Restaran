from django.urls import path
from .views import MenuView, ManlsView


urlpatterns = [
    path('',MenuView.as_view(), name='menu'),
    # path('category/create/', CategoryCreateView.as_view(), name='category/create'),
    # path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category/update'),
    # path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category/delete'),
    path('manls/', ManlsView.as_view(), name='manls'),
    # path('manls/create/', ManlsCreateView.as_view(), name='manls/create'),
    # path('manls/update/<int:pk>/', ManlsUpdateView.as_view(), name='manls/update'),
    # path('manls/delete/<int:pk>/', ManlsDeleteView.as_view(), name='manls/delete'),    
]