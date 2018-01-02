from django import template
from django.db.models.aggregates import Count

from articles.models import Article, Category, Tag

register = template.Library()


@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.all()[:num]


@register.simple_tag
def get_categorys():
    return Category.objects.annotate(num=Count('articles'))


@register.simple_tag
def get_archives():
    return Article.objects.dates('add_time', 'month')


@register.simple_tag
def get_tags():
    return Tag.objects.all()
