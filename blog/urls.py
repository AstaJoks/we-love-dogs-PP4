from . import views
from django.urls import path
from .views import CreatePost, UpdatePost, DeletePost
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('create/', CreatePost.as_view(), name="create_post"),
    path('post/edit/<int:pk>', UpdatePost.as_view(), name="update_post"),
    path('post/<int:pk>/delete', DeletePost.as_view(), name="delete_post"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]

handler404 = 'blog.views.handler404'
