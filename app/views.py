from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import authentication
from .serializers import UsersSerializer
from .models import Users

class HomeView(viewsets.ViewSet):
    
    def home(self, request):
        return render(request, 'home.html')
    
    def register(self, request):
        if request.method == 'POST':
            serializer = UsersSerializer(data=request.POST)
            if serializer.is_valid():
                serializer.save()
                
                username = request.POST.get('username')
                password = request.POST.get('password')
                
                # Crear un usuario en el sistema de autenticación de Django
                user = User.objects.create_user(username=username, password=password)
                
                # Autenticar y loguear al usuario
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')
        
        else:
            serializer = UsersSerializer()
            
        return render(request, 'register.html', {'serializer': serializer})
    
    def login(self,request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'home.html', {'error':'Invalid Credentials'})
            
        return render(request,'home.html')
            

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
