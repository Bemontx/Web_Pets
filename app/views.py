from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import authentication
from .serializers import UsersSerializer, PetsSerializer
from .models import Users, Pets

# Create your views here.
class IndexView(viewsets.ViewSet):
    permission_classes = [AllowAny]
    authentication_classes = [authentication.SessionAuthentication]

    def list(self, request):
        queryset = Users.objects.all()
        serializer = UsersSerializer(queryset, many=True)
        context = {
            'users': serializer.data
        }
        return render(request, 'index.html', context)
class HomeView(viewsets.ViewSet):
    
    def home(self,request):
        return render(request,'home.html')
