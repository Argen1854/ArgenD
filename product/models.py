from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField


class CallBack(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    data = models.DateField(auto_now_add=True)
    callback = models.BooleanField(default=False)

    def __str__(self):
        return str(self.callback)


class CollectionProducts(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class Product(models.Model):
    title = models.CharField(max_length=50)
    text = RichTextField()
    vendor_code = models.CharField(max_length=50)
    size_range = models.CharField(max_length=30)
    cloth = models.CharField(max_length=30)
    quantity_in_line = models.IntegerField()
    material = models.CharField(max_length=30)
    checkbox_hit = models.BooleanField()
    checkbox_new = models.BooleanField(default=True)

    collection = models.ForeignKey(CollectionProducts, on_delete=models.CASCADE, related_name='products', null=True, blank=True)

    price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)
    discount_price = models.IntegerField(null=True, blank=True)
    new_price = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.discount:
            self.new_price = self.price - ((self.price//100) * self.discount)
            self.discount_price = (self.price//100) * self.discount
        super(Product, self).save(*args, **kwargs)


    @property
    def get_images(self):
        images = ImageProducts.objects.filter(product=self)
        return [{'id': i.id, 'image': i.image.url, 'color': i.color} for i in images]


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ImageProducts(models.Model):
    image = models.ImageField(upload_to='')
    color = ColorField(default='#FF0000')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")


class Slider(models.Model):
    image = models.ImageField(upload_to="")
    link = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Слайдер'



