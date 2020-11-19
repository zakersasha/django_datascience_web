from django.shortcuts import render, redirect

from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView


def applicationsview(request):
    applications = Article.objects.all()
    return render(request, 'news/news_home.html', {'applications': applications})


class RequestDetailView(DetailView):
    model = Article
    template_name = 'news/news_detail.html'
    context_object_name = 'article'


class RequestUpdateView(UpdateView):
    model = Article
    template_name = 'news/news_update.html'

    form_class = ArticleForm


class RequestDeleteView(DeleteView):
    model = Article
    success_url = '/applications/'
    template_name = 'news/news_delete.html'


def addrequest(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('applications')
        else:
            error = 'Ошибка формы'

    form = ArticleForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/add_news.html', data)
