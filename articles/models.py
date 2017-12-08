from datetime import datetime

from django.db import models


class Category(models.Model):
    """
    标签模型
    """
    name = models.CharField(max_length=30, verbose_name='标签')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    文章模型
    """
    category = models.ForeignKey(Category, related_name='articles')
    title = models.CharField(max_length=64, verbose_name='标题')
    content = models.TextField(null=True, blank=True, verbose_name='正文')
    content_html = models.TextField(
        null=True, blank=True, verbose_name='正文MarkDown')
    add_time = models.DateField(default=datetime.now)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
