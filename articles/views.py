from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from articles.models import Article, Category


class IndexView(View):
    """
    首页视图
    """

    def get(self, request):
        articles = Article.objects.all()
        return render(request, 'index.html', {
            'articles': articles,
        })


class ArchiveView(View):
    """
    归档视图
    """

    def get(self, request, year, month):
        articles = Article.objects.filter(
            add_time__year=year,
            add_time__month=month
        )
        return render(request, 'index.html', {
            'articles': articles,
        })


class CategoryView(View):
    """
    分类视图
    """

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        articles = category.articles.all()
        return render(request, 'index.html', {
            'articles': articles,
        })


class DetailView(View):
    """
    详情视图
    """

    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        return render(request, 'detail.html', {
            'article': article,
        })

    def post(self, request):
        """
        发表评论
        """
        pass
