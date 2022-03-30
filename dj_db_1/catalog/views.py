from django.shortcuts import render
from dj_db_1.catalog.models import Phone

# Create your views here.


def show_catalog(request):
    sort_ = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort_ == 'low':
        phones = phones.order_by('price')
    elif sort_ == 'high':
        phones = phones.order_by('-price')

    context = {
        'phones': phones,
    }
    template = 'catalog.html'
    return render(request, template, context)


def show_item(request, slug):
    template = 'item.html'
    phone = Phone.objects.filter(slug__contains=slug)
    context = {
        'phone': phone,
    }

    return render(request, template, context)
