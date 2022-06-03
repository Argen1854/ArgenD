from decimal import Decimal
from django.conf import settings
from product.models import Product, ImageProducts


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    

    def add(self, product, image_id, quantity=1, update_quantity=False):
        product_id = str(product.id)
        image = ImageProducts.objects.get(id=image_id)
        if product_id in self.cart:
            self.cart[product_id]['image'].append({'id':image_id,
                                    'color': image.color,
                                    'image': image.image.url})
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                    'price': str(product.price),
                                    'image': [{'id':image_id,
                                    'color': image.color,
                                    'image': image.image.url}],
                                    'discount_price': str(product.discount_price),
                                    'quantity_in_line': str(product.quantity_in_line)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()


    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    
    def remove(self, product, image_id):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def get_all(self):
        product_ids = self.cart.keys()
        return product_ids
    
    def get_total_price(self):
        price = sum(Decimal(item['price']) * item['quantity'] for item in
                self.cart.values())
        discount = sum(Decimal(item['discount_price']) * item['quantity'] for item in
                self.cart.values())
        quantity_in_line = sum(Decimal(item['quantity_in_line']) * item['quantity'] for item in 
                self.cart.values())
        quantity = sum(Decimal(1) * item['quantity'] for item in 
                self.cart.values())
        
        return {'price': price, 'discount_price': discount, 'quantity_in_line': quantity_in_line, 'quantity': quantity}

    
    def clear(self):
        # удаление корзины из сессии
        self.cart = self.session[settings.CART_SESSION_ID] = {}
        self.save()