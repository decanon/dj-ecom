from django.shortcuts import render


def store(request):
    context = {}
    return render(request, 'dj_store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'dj_store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'dj_store/checkout.html', context)
