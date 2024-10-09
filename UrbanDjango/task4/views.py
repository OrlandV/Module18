from django.shortcuts import render


def platform(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'fourth_task/platform.html', context)


def games(request):
    context = {
        'title': 'Игры',
        'items': ['Игра1', 'Игра2', 'Игра3']
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    context = {
        'title': 'Корзина',
    }
    return render(request, 'fourth_task/cart.html', context)
