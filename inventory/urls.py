from django.urls import path
from .views import InventoryCreateView, InventoryListView, InventoryDetailView, InventoryPerOwner, InventoryPerAdmin, InventoryPerSeller, GetUser, GetUsername

urlpatterns = [
    path('create/', InventoryCreateView.as_view()),
    path('list/', InventoryListView.as_view()),
    path('detail/<int:pk>', InventoryDetailView.as_view()),
    path('owner/<int:id_owner>', InventoryPerOwner.as_view()),
    path('admin/<int:id_admin>', InventoryPerAdmin.as_view()),
    path('seller/<int:id_seller>', InventoryPerSeller.as_view()),
    path('user/<str:username>', GetUser.as_view()),
    path('username/<int:id>', GetUsername.as_view()),
]