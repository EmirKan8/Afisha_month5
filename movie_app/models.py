from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя директора")

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название фильма")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    duration = models.PositiveIntegerField(default=0, verbose_name="продолжительность")
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(max_length=1000, verbose_name="Коментарии")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

