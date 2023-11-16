from django.shortcuts import render
from .models import Custom
# Create your views here.

def main(request):
    nars = Custom.objects.all()
    context = {
        'nars':nars,
    }
    return render(request, 'home.html', context=context)