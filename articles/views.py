from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from articles.models import Article


class IndexView(View):
    """
    首页视图
    """

    def get(self, request):
        articles = Article.objects.all()
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
