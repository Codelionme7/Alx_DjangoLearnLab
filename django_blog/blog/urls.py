from django.urls import path
from .views import PostListView, PostByTagListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # Search is handled by the main list view with ?q= parameter
    path('', PostListView.as_view(), name='post-list'),
    
    # Tagging URL
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post-by-tag'),
    
    # ... existing URLs ...
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # ...
    # Search URL (optional specific path, but usually handled by root)
    path('search/', PostListView.as_view(), name='search-posts'),
]
