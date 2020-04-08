from django.urls import path
from blog import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView


urlpatterns = [
    path('',PostListView.as_view(),name='blog_home'),
    path('user/<str:username>',UserPostListView.as_view(),name='user_posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('post/new/',PostCreateView.as_view(),name='post_create'), # post_form.html
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post_update'), #post_form.html
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post_delete'),  # post_confirm_delete
    path('about/',views.about,name='blog_about'),
]
