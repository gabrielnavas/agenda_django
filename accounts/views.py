from django.shortcuts import render
from django.contrib import messages

def index(request):
  return render(request, 'accounts/index.html')

def login(request):
  return render(request, 'accounts/login.html')

def logout(request):
  return render(request, 'accounts/logout.html')

def signup(request):
  post = request.POST
  print(post)
  messages.success(request, 'olá mundo')
  return render(request, 'accounts/signup.html')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')
