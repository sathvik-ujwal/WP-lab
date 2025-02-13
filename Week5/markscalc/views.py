from django.shortcuts import render

def index(request):
    return render(request, 'mark.html')

# Create your views here.
