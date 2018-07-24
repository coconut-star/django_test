from django.shortcuts import render
from apps.hedgetrade import views
from apps.hedgetrade import models
# Create your views here.
def dashboard(request):
    orders = models.HedgeOrder.objects.all()
    return render(request, 'hedgetrade/dashboard.html',{'orders':orders})


def addOrder(request):
    site1 = request.POST.get('site1')
    site2 = request.POST.get('site2')
    type1 = request.POST.get('type1')
    type2 = request.POST.get('type2')
    newOrder = models.HedgeOrder()
    newOrder.site1 = site1
    newOrder.site2 = site2
    newOrder.type1 = type1
    newOrder.type2 = type2
    newOrder.save()
    return render(request, 'hedgetrade/dashboard.html')
