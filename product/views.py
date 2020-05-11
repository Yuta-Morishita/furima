
from django.views import generic
from .models import Item, Images
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'product/index.html'
    model = Item
    context_object_name = 'items'


# class CreateView(generic.CreateView):
#     template_name = 'product/create.html'
#     model = ItemModel, ImageModel
#     fields = ('name', 'price', 'ability', 'status', 'shipping_burden', 'shipping_area', 'shipping_days', 'src')
#     success_url = reverse_lazy('product:list')


class ListView(generic.ListView):
    template_name = 'product/list.html'
    model = Item

    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'images_list': Images.objects.all()
        })
        items = Item.objects.all()
        return context

    def get_queryset(self):
        return Item.objects.all()


class DetailView(generic.DetailView):
    template_name = 'product/detail.html'
    model = Item


# class UpdateView(generic.UpdateView):
#     template_name = 'product/update.html'
#     model = ItemModel
#     fields = ('name', 'price', 'ability', 'status',)
#     success_url = reverse_lazy('product:list')


class DeleteView(generic.DeleteView):
    template_name = 'product/delete.html'
    model = Item
    success_url = reverse_lazy('product:list')
