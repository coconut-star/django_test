from django.shortcuts import render
from apps.hedgetrade import views

# Create your views here.
def dashboard(request):
    return render(request, 'hedgetrade/dashboard.html')
