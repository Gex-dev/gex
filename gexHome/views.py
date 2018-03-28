from django.shortcuts import render

def home(request):
    return render(request, 'landingPage/home.html')
    
def construction(request):
    return render(request, 'landingPage/construction.html')