
from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('create/', CreateView.as_view(), name='create'),
    path('list/', views.ListView.as_view(), name='list'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/update/', UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete')
]
