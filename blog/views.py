from django.shortcuts import render
from django.views import generic
from .models import Post


class Home(View):
    """
    Renders the home page of the website
    """
    def get(self, request):
        return render(request, "index.html")
