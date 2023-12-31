from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm, EditPostForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class Home(View):
    """
    Renders the home page of the website
    """
    def get(self, request):
        return render(request, "index.html")


class PostList(generic.ListView):
    """View to render a Blog Posts List"""
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 6


class CreatePost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """View to create the post by the user"""
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_message = 'Your post has been successfully created!'

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super(CreatePost, self).form_valid(form)


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin,
                 SuccessMessageMixin, UpdateView):
    """View to edit the users post"""
    model = Post
    template_name = 'edit_post.html'
    form_class = EditPostForm
    success_message = 'Your post has been successfully updated!'
    """ Test user is author or throw 403 """
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author \
            or self.request.user.is_superuser


class DeletePost(LoginRequiredMixin, UserPassesTestMixin,
                 SuccessMessageMixin, DeleteView):
    """View to delete the users post"""
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')
    success_message = "Your post has been successfully deleted!"

    def delete(self, request, *args, **kwargs):
        """Function for succcess message"""
        messages.success(self.request, self.success_message)
        return super(DeletePost, self).delete(request, *args, **kwargs)
    """ Test user is author or throw 403 """
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author \
            or self.request.user.is_superuser


class PostDetail(LoginRequiredMixin, View):
    """View to render a Blog Posts Details"""

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """Function for users to allow commenting"""
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, "Comment Added Successfully!")
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(LoginRequiredMixin, View):
    """Function for users to allow liking the post"""
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def handler404(request, exception):
    """
    Displays a custom 404 error page.
    """
    return render(request, '404.html', status=404)


def handler500(request, exception):
    """
    Displays a custom 500 error page.
    """
    return render(request, '500.html', status=500)
