from django.shortcuts import render


def platform(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'platform.html', context)


def games(request):
    context = {
        'title': 'Игры',
        'item1': 'Игра1',
        'item2': 'Игра2',
        'item3': 'Игра3'
    }
    return render(request, 'games.html', context)


def cart(request):
    context = {
        'title': 'Корзина',
    }
    return render(request, 'cart.html', context)
