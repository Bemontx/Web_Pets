from django.shortcuts import render,redirect
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import authentication
from .serializers import UsersSerializer, PetsSerializer
from .models import Users, Pets

# Create your views here.
class HomeView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    authentication_classes =[authentication.SessionAuthentication]
    permission_classes = [AllowAny]
    
    def get(self,request,*args, **kwargs):
        context={}
        return render(request,'home.html',context)
