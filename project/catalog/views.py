from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from catalog.models import Product


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/products_list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(is_active=True)


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        # product.delete()
        product.is_active = False
        product.save()
        return redirect('catalog:products_list')
    return redirect('catalog:products_list')
