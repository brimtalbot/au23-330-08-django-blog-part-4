from django.urls import path
from .views import detail_view, BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_index"),
    path('posts/<int:post_id>/', BlogDetailView.as_view(), name="blog_detail"),
]
