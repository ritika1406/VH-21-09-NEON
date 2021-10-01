from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'stats.html')
    
def ambulance(request):
    return render(request, 'ambulance.html')