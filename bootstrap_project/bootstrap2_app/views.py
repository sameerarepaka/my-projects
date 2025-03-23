from django.shortcuts import render
from .models import Product  # Adjust the import based on your models structure

def product_list(request):
    if not Product.objects.exists():
        Product.objects.create(name='Sony WH-1000XM5', description='Industry-leading noise-canceling headphones', price='349')
        Product.objects.create(name='Apple MacBook Pro 16-inch', description='Powerful laptop with Apple M1 Pro chip', price='2499')
        Product.objects.create(name='Adidas NMD_R1', description='Stylish sneakers with boost cushioning', price='130')
        Product.objects.create(name='Puma Speed 600 Ignite', description='High-performance running shoes with responsive cushioning', price='120')
        Product.objects.create(name='Apple iPad Pro 12.9', description='Versatile tablet with Liquid Retina XDR display', price='1099')

    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


# Create your views here.
