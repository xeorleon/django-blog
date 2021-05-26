from django.db import models


class Post(models.Model):
    title = models.CharField("Başlık", max_length=120)
    content = models.TextField("İçerik")
    publishing_date = models.DateTimeField("Yayımlanma Tarihi")

    def __str__(self):
        return self.title
