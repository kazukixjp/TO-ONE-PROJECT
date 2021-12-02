from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField('本文')
    created = models.DateField('作成日', default=timezone.now)

    def __str__(self):
        return self.title

# 新しく作ったmodel


# class Postnew(models.Model):
#     parent_dir = models.CharField("親ディレクトリ", max_length=10)
#     child_dir = models.CharField("子ディレクトリ", max_length=10)
#     link = models.CharField("リンク")
#     link_title = models.CharField("リンクのタイトル", max_length=22)
