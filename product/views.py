
from django.views.generic import
from .models import ItemModel, ImageModel
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'product/index.html'
    model = ItemModel


class CreateView(CreateView):
    template_name = 'product/create.html'
    model = ItemModel, ImageModel
    fields = ('name', 'price', 'ability', 'status', 'shipping_burden', 'shipping_area', 'shipping_days', 'src')
    success_url = reverse_lazy('product:list')


class ListView(ListView):
    template_name = 'product/list.html'
    model = ItemModel


class DetailView(DetailView):
    template_name = 'product/detail.html'
    model = ItemModel


class UpdateView(UpdateView):
    template_name = 'product/update.html'
    model = ItemModel
    fields = ('name', 'price', 'ability', 'status',)
    success_url = reverse_lazy('product:list')


class DeleteView(DeleteView):
    template_name = 'product/delete.html'
    model = ItemModel
    success_url = reverse_lazy('product:list')
