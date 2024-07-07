from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    response_get = request.GET

    sort = response_get.get('sort')

    if sort:
        obj_phones = Phone.objects.all().order_by(sort)
    else:
        obj_phones = Phone.objects.all()

    context = {
        'phones': obj_phones,
    }

    return render(request, 'catalog.html', context)


def show_product(request, slug):
    obj_phone = get_object_or_404(Phone, slug=slug)

    context = {
        'phone': obj_phone,
    }

    return render(request, 'product.html', context)
