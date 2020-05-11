
from django.views import generic
from .models import Item, Images
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'product/index.html'
    model = Item, Images


# class CreateView(generic.CreateView):
#     template_name = 'product/create.html'
#     model = ItemModel, ImageModel
#     fields = ('name', 'price', 'ability', 'status', 'shipping_burden', 'shipping_area', 'shipping_days', 'src')
#     success_url = reverse_lazy('product:list')


class ListView(generic.ListView):
    template_name = 'product/list.html'
    model = Item, Images


class DetailView(generic.DetailView):
    template_name = 'product/detail.html'
    model = Item, Images


# class UpdateView(generic.UpdateView):
#     template_name = 'product/update.html'
#     model = ItemModel
#     fields = ('name', 'price', 'ability', 'status',)
#     success_url = reverse_lazy('product:list')


class DeleteView(generic.DeleteView):
    template_name = 'product/delete.html'
    model = Item, Images
    success_url = reverse_lazy('product:list')
