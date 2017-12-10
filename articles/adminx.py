import xadmin
from articles.models import Category, Article, Comment


class CategoryAdmin:
    list_display = ['name', 'add_time']
    search_fields = ['name', 'add_time']
    list_filter = ['name', 'add_time']


class ArticleAdmin:
    list_display = ['title', 'category', 'add_time']
    search_fields = ['title', 'content', 'add_time']
    list_filter = ['title', 'category', 'add_time']


class CommentAdmin:
    list_display = ['article', 'username', 'email', 'add_time']
    search_fields = ['article', 'email', 'add_time']
    list_filter = ['article', 'username', 'email', 'add_time']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Comment, CommentAdmin)
