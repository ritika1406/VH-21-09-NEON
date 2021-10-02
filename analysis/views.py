from django.shortcuts import render
from .models import *
from django.http.response import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'stats.html')

def ambulance(request):
    return render(request, 'ambulance.html')

def beds(request):
    return render(request, 'beds.html')

def icubeds(request):
    return render(request, 'icubeds.html')

def oxygen(request):
    return render(request, 'oxygen.html')

def plasma(request):
    return render(request, 'plasma.html')
def graph(request):
    return render(request, 'graph.html')

def patient_status(request):
    allPosts = Patient_Status.objects.all()
    params = {'allPosts': allPosts}
    return render(request, 'patient_status.html', params)
    

def search(request):
    query = request.GET['search']
    allPosts = Ambulance.objects.filter(district__icontains=query)
    params = {'allPosts': allPosts}
    return render(request, 'search.html', params)

def search_beds(request):
    query = request.GET['search_beds']
    allPosts = Beds.objects.filter(district__icontains=query)
    params = {'allPosts': allPosts}
    return render(request, 'search.html', params)

def search_icu(request):
    query = request.GET['search_icu']
    allPosts = ICU_Beds.objects.filter(district__icontains=query)
    params = {'allPosts': allPosts}
    return render(request, 'search.html', params)

def search_plasma(request):
    query = request.GET['search_plasma']
    allPosts = Plasma.objects.filter(district__icontains=query)
    params = {'allPosts': allPosts}
    return render(request, 'search.html', params)

def search_oxygen(request):
    query = request.GET['search_oxygen']
    allPosts = Oxygen.objects.filter(district__icontains=query)
    params = {'allPosts': allPosts}
    return render(request, 'search.html', params)
