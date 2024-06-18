from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import HomeView

router = DefaultRouter()
router.register(r'home', HomeView)

app_name = 'index'

urlpatterns = [
    path('', HomeView.as_view({'get': 'list'}), name='home'),
]

urlpatterns += router.urls