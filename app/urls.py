from django.urls import path
from .views import IndexView, HomeView, RegisterView

urlpatterns = [
    path('', HomeView.as_view({'get': 'home', 'post': 'home'}), name='home'),
    path('index/', IndexView.as_view({'get': 'list'}), name='index'),
    path('register/', RegisterView.as_view({'get': 'register', 'post': 'register'}), name='register'),
]
