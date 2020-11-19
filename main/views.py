from django.shortcuts import render


def home(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'body', 'once']
    }
    return render(request, 'main/home.html', data)


def about(request):
    data = {
        'title': 'О нас'
    }
    return render(request, 'main/about.html', data)


def contacts(request):
    data = {
        'title': 'Команда Курабье'
    }
    return render(request, 'main/contacts.html', data)


def statistics(request):
    data = {
        'title': 'Статистика'
    }
    return render(request, 'main/stat.html', data)
