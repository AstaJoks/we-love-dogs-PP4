from django.shortcuts import render
from django.views import generic, View
from .models import Post


class Home(View):
    """
    Renders the home page of the website
    """
    def get(self, request):
        return render(request, "index.html")


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 6
