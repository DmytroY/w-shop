from django.conf import settings
from wap.models import Product
from decimal import Decimal

class Cart(object):
    def __init__(self, request):
        """Initializing Cart"""
        self.session=request.session
        # try to get session
        cart = self.session.get(settings.CART_SESSION_ID)
        # if there are no session,  -> create session with empty cart
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        """adding new product to the cart"""
        product_id = str(product.code)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, "price":str(product.price)}

        """put q'ty of products or 
        increment q'ty if we add of already existing product"""
        if override_quantity:
            self.cart[product_id][quantity] = quantity
        else:
            self.cart[product_id][quantity] += quantity
        self.save()

    def remove(self, product):
        """remove product from cart if existed"""
        product_id = str(product.code)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        """ create an iterator which yields items in the cart and calculate amount as price * q'ty"""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.code)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """ return ttl q'ty of products in the cart"""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """ return total price for all products in the cart"""
        return sum(Decimal(item['price'] * item['quantity'] for item in self.cart.values()))

    def clear(self):
        """clear cart"""
        del self.session[settings.CART_SESSIONS_ID]
        self.save()

