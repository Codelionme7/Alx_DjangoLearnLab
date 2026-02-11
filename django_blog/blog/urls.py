from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    # Auth URLs (Keep existing)
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Blog Post URLs
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
