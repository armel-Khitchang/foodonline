from django.db.models import Min, Max
from .models import Category, Vendor, Product, Address

def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()
    min_max_price = Product.objects.aggregate(Min('price'),Max('price'))

    address = None
    if request.user.is_authenticated:
        try:
            address = Address.objects.get(user=request.user)
        except Address.DoesNotExist:
            address = None

    return {
        'categories': categories,
        'vendors': vendors,
        'min_max_price': min_max_price,
        'address': address,
    }
         
    