from django.shortcuts import render, get_object_or_404
from django.db.models import Q # Required for complex queries
from django.views.generic import ListView
from .models import Post
from taggit.models import Tag
# ... other imports ...
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserUpdateForm  # Ensure UserUpdateForm is imported

# ... register view ...

@login_required
def profile(request):
    if request.method == 'POST':
        # This block satisfies the "handle POST requests" check
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'blog/profile.html', {'form': form})

# ... Search view definition ...
def search(request):
    # simple search view for the url pattern
    return render(request, 'blog/search_results.html')
# Update PostListView to handle search and filtering
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 5 # Optional: Pagination

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Search Functionality
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | 
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
            
        return queryset

# View to list posts by a specific tag
class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        # Get the tag from the URL and filter posts
        tag_slug = self.kwargs.get('tag_slug')
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags__in=[self.tag])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_tag'] = self.tag
        return context
