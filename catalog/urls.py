
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('managment.urls')),
    path('about/', include('managment.urls')),
    path('photos/', include('managment.urls')),
    
    path('create/', include('managment.urls')),
    path('create-client/', include('managment.urls')),
    path('create-clothing/', include('managment.urls')),
    path('create-category/', include('managment.urls')),

    path('update/<int:pk>/', include('managment.urls')),
    path('update-client/<int:pk>/', include('managment.urls')),
    path('update-clothing/<int:pk>/', include('managment.urls')),
    path('update-category/<int:pk>/', include('managment.urls')),
    
    path('delete/<int:pk>/', include('managment.urls')),
    path('delete-client/<int:pk>/', include('managment.urls')),
    path('delete-clothing/<int:pk>/', include('managment.urls')),
    path('delete-category/<int:pk>/', include('managment.urls')),
    
    path('', include('usuario.urls')),
]