from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.utils import timezone


from .models import Product, OrderProduct, Order, OrderAdress, Category
from account.models import  UserAddress, User
from django import  template
from django.db.models import Q
import pickle
# Create your views here.


def index(request):
    all_entry = Product.products.all()
    cat = request.GET.get('category')
    if request.GET.get('q') is not None:
        q=request.GET.get('q')
        return HttpResponseRedirect('/shop?q='+q)
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


def OrderView(request):
    if request.method == 'POST':
        id = request.POST.get('productid')
        print(id)
        quant =int (request.POST.get('quantity'))
        print(quant)
        order_product = OrderProduct.objects.filter(id=id)
        t=OrderProduct.objects.get(id=id)
        name=t.product.name
        product= Product.products.get(name=name)
        print(product.number)
        max = int(product.number)
        if quant>max:
            order_product.update(quantity=max)
        else:
            order_product.update(quantity=quant)
        return redirect('/cart')

    else:

        order = Order.objects.filter(user=request.user, ordered=False)
        order_products = OrderProduct.objects.filter(user=request.user, ordered=False)
        total = 0
        for se in order_products:
             print(se.product.name)
             total += se.quantity * se.product.price
        return render(request, "cart.html", {'cart': order, 'product': order_products, 'total': total})



class ItemDetailView(DetailView):
    model = Product
    template_name = "product.html"

def add_to_cart(request, slug):





    if request.user.is_authenticated:

        product = get_object_or_404(Product, slug=slug)
        order_product, created = OrderProduct.objects.get_or_create(product=product,
                                                       user=request.user,
                                                       ordered=False)
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]

            if order.products.filter(product__slug=product.slug).exists():
                quant= int(product.number)

                if int(order_product.quantity)+1 <= quant:
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

        user=request.user
        order=get_object_or_404(Order, user=user, ordered=False)

        order_products=OrderProduct.objects.all()
        order_products=order_products.filter(user=user, ordered=False)

        total=0
        for se in order_products:
            print(se.product.name)
            total += se.quantity*se.product.price

        return render(request, "cartadd.html", {'cart':order, 'product':order_products, 'total':total})

    else:
        print(request.get_full_path())
        url=request.get_full_path()
        return redirect('/account/login?url='+url)


def updateQuantity(request, slug):
    print("To tutaj bylem!")
    id=request.POST.get('productid')
    quant = request.POST.get('quantity')
    print(id)

    order_product=OrderProduct.objects.filter(id=id)
    order_product.update(quantity=quant)



    print('Ilosc: '+ quant)
    return  redirect('/cart')

def cartupdateQuantity(request):
    print("JEstem ty")
    id = request.POST.get('productid')
    print(id)
    if request.method == 'POST':
        id = request.POST.get('productid')
        print(id)
        quant = request.POST.get('quantity')
        print(quant)
        order_product = OrderProduct.objects.filter(id=id)
        order_product.update(quantity=quant)

        return redirect('cart')

@login_required(login_url='account/login')
def buy(request):
    print(request.user)
    user = User.objects.get(username=request.user)
    useradress=UserAddress.objects.get(user=request.user)
    order_products = OrderProduct.objects.filter(user=request.user, ordered=False)
    total = 0
    for se in order_products:
        print(se.product.name)
        total += se.quantity * se.product.price

    return render(request, 'buy.html', {'adres':useradress, 'user':user, 'products':order_products, 'total':total})


def purchase(request):
    if request.method=='POST':
        print("Siemanko")
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        city = request.POST['city']
        street = request.POST['street']
        address = request.POST['address']
        zipcode = request.POST['zipcode']
        phone = request.POST['phone']
        print(phone)







        orderaddress = OrderAdress.objects.create(order=Order.objects.get(user=request.user, ordered=False), firstname=firstname, lastname=lastname, city=city, street=street, address=address, zipcode=zipcode, phone=phone, )
        order = Order.objects.filter(user=request.user, ordered=False).update(ordered=True)
        order_products = OrderProduct.objects.filter(user=request.user, ordered=False)
        for prod in order_products:
            produkt =prod.product.name
            numbero = prod.product.number
            ilosc = prod.quantity
            Product.products.filter(name=produkt).update(number=numbero-ilosc)
        order_products = OrderProduct.objects.filter(user=request.user, ordered=False).update(ordered=True)
        OrderAdress.objects.create()


        return redirect('/')
    else:
        return redirect('/')



def categoryLaptops(request, slug):
    
    category = Category.objects.all()
    clist=[]
    for  c in category:
        clist.append(c.name)
    print(category)
    categorycount=clist.count(slug)
    print(clist.count(slug))
    if categorycount >0:

        category = Category.objects.get(name=slug)
        products = Product.products.filter(category=category)
        print(products)

        return render(request, 'shop.html', {'category':products})

    else:
        products =Product.products.all()
        return render(request, 'shop.html' )

def search(request):

    print("Bylem w search")
    query=request.GET.get('q')
    print(query)
    if query is not None:
        results = Product.products.filter(Q(name__icontains=query))


        return render(request, "shop.html", {'category':results})
    else:
        products=Product.products.all()
        return render(request, "shop.html", {'category':products})

def shop(request):
    products = Product.products.all()
    return render(request, 'shop.html', {'category': products})


def delete(request):
    if request.method=='POST':
        productid = request.POST.get('product')
        print(productid)
        OrderProduct.objects.filter(id=productid).delete()

        order = Order.objects.filter(user=request.user, ordered=False)
        order_products = OrderProduct.objects.filter(user=request.user, ordered=False)
        total = 0
        for se in order_products:
            print(se.product.name)
            total += se.quantity * se.product.price

        return redirect('/cart')

def deleteAdd(request, slug):
    if request.method=='POST':
        productid = request.POST.get('product')
        print(productid)
        OrderProduct.objects.filter(id=productid).delete()

        order = Order.objects.filter(user=request.user, ordered=False)
        order_products = OrderProduct.objects.filter(user=request.user, ordered=False)
        total = 0
        for se in order_products:
            print(se.product.name)
            total += se.quantity * se.product.price

        return redirect('/cart')

def userProfile(request):
    user=request.user
    userobject= User.objects.get(username=user)

    adress=UserAddress.objects.get(user=userobject.id)
    print(user)
    print(userobject.username)
    return render(request, 'user.html', {'user':userobject, 'adres':adress})