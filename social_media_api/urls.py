from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # User Authentication
    path('api/users/', include('accounts.urls')),
    
    # Posts and Comments (This handles the CRUD check)
    path('api/', include('posts.urls')),
]
