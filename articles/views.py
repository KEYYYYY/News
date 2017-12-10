from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from articles.models import Article, Category
from articles.forms import CommentForm


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
        article.view_count += 1
        article.save()
        comment_form = CommentForm()
        return render(request, 'detail.html', {
            'article': article,
            'form': comment_form,
        })

    def post(self, request, article_id):
        """
        发表评论
        """

        article = get_object_or_404(Article, id=article_id)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('detail', article_id=article_id)
        return render(request, 'detail.html', {
            'article': article,
            'form': comment_form,
        })
