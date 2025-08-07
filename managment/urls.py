from django.urls import path
from .views import AdminCreate, AdminDelete, AdminUpdate, CategoryCreate, CategoryDelete, CategoryUpdate, ClientCreate, ClientDelete, ClientUpdate, ClothingCreate, ClothingDelete, ClothingUpdate, ClothingList, IndexView, AboutView, PhotosList

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),


    # list
    path('photos/', PhotosList.as_view(), name="photos"),
    path('clothing-list/', ClothingList.as_view(), name="clothing-list"),
    
    # create
    path('create/', AdminCreate.as_view(), name="create"),
    path('create-client/', ClientCreate.as_view(), name="create-client"),
    path('create-clothings/', ClothingCreate.as_view(), name="create-clothing"),
    path('create-category/', CategoryCreate.as_view(), name="create-category"),
    
    # update
    path('update/<int:pk>/', AdminUpdate.as_view(), name="update"),
    path('update-client/<int:pk>/', ClientUpdate.as_view(), name="update-client"),
    path('update-clothing/<int:pk>/', ClothingUpdate.as_view(), name="update-clothing"), 
    path('update-category/<int:pk>/', CategoryUpdate.as_view(), name="update-category"), 
    
    
    #delete 
    path('delete/<int:pk>/', AdminDelete.as_view(), name="delete"),
    path('delete-client/<int:pk>/', ClientDelete.as_view(), name="delete-client"),
    path('delete-clothing/<int:pk>/', ClothingDelete.as_view(), name="delete-clothing"), 
    path('delete-category/<int:pk>/', CategoryDelete.as_view(), name="delete-category"),
    
]
