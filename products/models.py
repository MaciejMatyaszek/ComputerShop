from django.db import models

# Create your models here.
from django.db import models

from django.conf import settings
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Nazwa Kategorii', max_length=100)
    slug = models.SlugField('Odnośnik', unique=True, max_length=100)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField('Nazwa Produktu', max_length=200)
    slug = models.SlugField('Odnośnik', unique=True, max_length=100)
    icon = models.ImageField('Ikona Produktu', upload_to='products/%Y/%m/%d')
    icon1 = models.ImageField('Zdjecie 1', upload_to='products/%Y/%m/%d', default=False)
    icon2 = models.ImageField('Zdjecie 2', upload_to='products/%Y/%m/%d', default=False)
    number = models.IntegerField('Liczba Sztuk')
    price = models.IntegerField('Cena')
    category = models.ManyToManyField(Category, verbose_name='Kategorie')
    products = models.Manager()


    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

    def __str__(self):
        return self.name

    def get_products(self):
        return "\n".join([p.name for p in self.category.all()])

    def __unicode__(self):
        return self.name

    def get_add_to_cart_url(self):
          return reverse("ComputerShop:add-to-cart", kwargs={ 'slug': self.slug})

class Customer(models.Model):
    name = models.TextField('Imie', max_length=15)
    surname = models.TextField('Nazwisko')
    slug = models.SlugField('Odnośnik', unique=True, max_length=100)
    products = models.ManyToManyField(Product, verbose_name='Produkty')
    category = models.Manager()

    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klienci"

    def __unicode__(self):
        return self.name


class OrderProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.quantity} of {self.product.name}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username



