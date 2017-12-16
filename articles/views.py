from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from articles.models import Article, Category
from articles.forms import CommentForm


class IndexView(ListView):
    """
    首页视图
    """
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'


class ArchiveView(ListView):
    """
    归档视图
    """
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchiveView, self).get_queryset().filter(
            add_time__year=year,
            add_time__month=month
        )


class CategoryView(ListView):
    """
    分类视图
    """
    model = Category
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return get_object_or_404(
            Category,
            id=self.kwargs.get('category_id')
        ).articles.all()


class ArticleDetailView(DetailView):
    """
    详情视图
    """

    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        # 阅读量 +1
        article.increase_views()
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
