from django.urls import path
from .views import ItemListView, ItemDetailView

urlpatterns=[
    path('item-list',ItemListView.as_view(), name='item-list' ),
    path('<int:pk>/item-detail', ItemDetailView.as_view(), name="item-detail"),
]