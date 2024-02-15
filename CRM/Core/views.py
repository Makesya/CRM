""" Autoimported modules """
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Indexed function"""
    return render(request=request, template_name="Core/index.html")
