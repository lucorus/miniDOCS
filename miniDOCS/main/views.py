from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from .models import *


def main_page(request):
    return render(request, 'main/main_page.html', {'language': Language.objects.all(), 'type': Type.objects.all()})


def search(request):
    search_query = request.GET.get('q')
    if search_query:
        tag = Tag.objects.filter(title__icontains=search_query)
    else:
        tag = Tag.objects.get(pk=0)
    #func = Func.objects.get(tag__title=tag)
    return render(request, 'language/tag.html', {'tag': tag, 'value': search_query, 'language': Language.objects.all()})


def language(request, language):
    func = Func.objects.filter(language__title=language)
    #func = search(request)
    return render(request, 'language/language.html', {'func': func, 'language': Language.objects.all(), 'lang': language})
