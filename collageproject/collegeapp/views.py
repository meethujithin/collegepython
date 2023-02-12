
from django.shortcuts import render,HttpResponse

# Create your views here.
def demo(request):
    return render(request,"index.html")