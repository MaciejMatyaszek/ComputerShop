from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.utils import timezone
from .models import Product, OrderProduct, Order

import pickle
# Create your views here.
def index(request):
    all_entry = Product.products.all()
    cat = request.GET.get('category')
    print(cat)
    cat_list = []
    if cat != None:

        for e in all_entry:
            print(cat)
            print(e.id)
            print(e.get_products())
            if cat == e.get_products():

                cat_list.append(e)
        return render(request, 'index.html', {'products': cat_list})
    for t in cat_list:
        print(t.id)

    else:
        return render(request, 'index.html', {'products': all_entry})


def ProductList(ListView):
    model = Product





class HomeView(ListView):
    model = Product
    paginate_by = 10
    template_name = "index.html"


class ItemDetailView(DetailView):
    model = Product
    template_name = "product.html"

def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_product, created = OrderProduct.objects.get_or_create(product=product,
                                                       user=request.user,
                                                       ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        if order.products.filter(product__slug=product.slug).exists():
            order_product.quantity += 1
            order_product.save()

        else:

            order.products.add(order_product)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,
                                     ordered_date=ordered_date)
        print(order_product)
        order.products.add(order_product)

    return redirect("ComputerShop:productdetail", slug=slug)



