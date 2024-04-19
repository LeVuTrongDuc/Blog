# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.list),
#     path('<int:id>/', views.post),
#     path("add_blog/", views.add_blogs, name="add_blog"),
# ]
from django.urls import path

from blog.models import Post
from blog import views

from django.views.generic import ListView

urlpatterns = [
    #post
    path('', ListView.as_view(
    queryset = Post.objects.all().order_by("-date"),
    template_name = 'blog/blog.html',
    context_object_name = 'Posts',
    paginate_by = 3,
    ), name='blog'),
    path('<int:id>/', views.post, name='post' ),
    path("add_blog/", views.add_blogs, name="add_blog"),
]
