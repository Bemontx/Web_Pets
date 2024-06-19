from django.urls import path, include
from .views import IndexView, HomeView

urlpatterns = [
    path('', HomeView.as_view({'get': 'home', 'post':'register'}), name='home'),
    path('index/', IndexView.as_view({'get': 'list'}), name='index'),
]
