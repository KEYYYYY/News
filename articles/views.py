from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

from articles.forms import CommentForm
from articles.models import Article, Category


class IndexView(ListView):
    """
    首页视图
    """
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'
    paginate_by = 3


class ArchiveView(ListView):
    """
    归档视图
    """
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'
    paginate_by = 3

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
    paginate_by = 3

    def get_queryset(self):
        return get_object_or_404(
            Category,
            id=self.kwargs.get('category_id')
        ).articles.all()


class ArticleDetailView(DetailView):
    """
    详情视图
    """
    model = Article
    template_name = 'detail.html'
    pk_url_kwarg = 'article_id'

    def get(self, request, *args, **kwargs):
        response = super(ArticleDetailView, self).get(request, *args, **kwargs)
        # 阅读量 +1
        self.object.increase_views()
        return response

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comments = self.object.comments.all()
        context.update({
            'form': form,
            'comments': comments,
        })
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            # 按理说这一应该是comment.artilce = article_object的
            # 但是已经获取到了article_id，再去数据库查询一次article显得多此一举
            comment.article_id = kwargs.get('article_id')
            comment.save()
            return redirect('detail', article_id=kwargs.get('article_id'))
        return render(request, 'detail.html', {
            'comment_form': comment_form,
        })
