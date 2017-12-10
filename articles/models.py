from datetime import datetime

from django.db import models
import markdown


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
    category = models.ForeignKey(
        Category, related_name='articles', verbose_name='类别')
    title = models.CharField(max_length=64, verbose_name='标题')
    content = models.TextField(null=True, blank=True, verbose_name='正文')
    content_html = models.TextField(
        null=True, blank=True, verbose_name='正文MarkDown')
    view_count = models.IntegerField(default=0, verbose_name='阅读量')
    comment_count = models.IntegerField(default=0, verbose_name='评论数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发表日期')

    class Meta:
        ordering = ('-add_time',)
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    # 重载save方法，保存的同时讲内容转化为html代码保存
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.content_html = markdown.markdown(
            self.content,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        super(Article, self).save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    评论模型
    """
    article = models.ForeignKey(Article, related_name='comments')
    username = models.CharField(max_length=32, verbose_name='用户名')
    email = models.EmailField(verbose_name='邮箱')
    url = models.URLField(null=True, blank=True, verbose_name='链接')
    content = models.TextField(verbose_name='内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')

    class Meta:
        ordering = ('-add_time',)
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
