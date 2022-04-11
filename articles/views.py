from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    article_query = Article.objects.all().\
        prefetch_related('scopes').order_by(ordering)
    context = {'object_list': article_query}
    return render(request, template, context)
