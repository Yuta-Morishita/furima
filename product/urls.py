
from django.urls import path
from . views import IndexView, CreateView, ListView, DetailView, UpdateView, DeleteView


app_name = 'product'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateView.as_view(), name='create'),
    path('list/', ListView.as_view(), name='list'),
    path('<int:pk>/detail/', DetailView.as_view(), name='detail'),
    path('<int:pk>/update/', UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete')
]
