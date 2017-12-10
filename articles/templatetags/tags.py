from django import template

from articles.models import Article, Category

register = template.Library()


@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.all()[:num]


@register.simple_tag
def get_categorys():
    return Category.objects.all()


@register.simple_tag
def get_archives():
    return Article.objects.dates('add_time', 'month')
