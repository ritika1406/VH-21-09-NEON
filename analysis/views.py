from django.shortcuts import render


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

