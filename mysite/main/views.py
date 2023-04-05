from django.shortcuts import render
from . models import Phons
# Create your views here.


def home(request):
    search_item = ''
    if request.method == 'POST':
        search_item = request.POST.get('search')
    phones = Phons.objects.filter(name__icontains=search_item)
    return render(request, 'main/index.html', context={
        'phones': phones,
        'search_item': search_item
    })