from . import views
from django.urls import path
from .views import CreatePost
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('create/', CreatePost.as_view(), name="create_post"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
