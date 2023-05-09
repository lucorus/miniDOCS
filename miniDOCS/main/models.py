from django.db import models
from django.urls import reverse, reverse_lazy


class Language(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('main', kwargs={'title': self.pk})


class Tag(models.Model):
    title = models.CharField(max_length=40)
    function = models.ManyToManyField('Func', blank=True)

    def __str__(self):
        return self.title


class Func(models.Model):
    func = models.CharField(max_length=100)
    description = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    type_return = models.CharField(max_length=20, blank=True)
    library = models.CharField(max_length=20, blank=True)

    def get_absolute_url(self):
        return reverse('main', kwargs={'language': self.pk})

    def __str__(self):
        return self.func


class Type(models.Model):
    title = models.CharField(max_length=40)
    size = models.CharField(max_length=2)
    range = models.CharField(max_length=250)
    value = models.CharField(max_length=200, default=0)

    def __str__(self):
        return self.title

