from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField


class CollectionProducts(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='')


    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=50)
    text = RichTextField()
    vendor_code = models.CharField(max_length=50)
    price = models.IntegerField()
    discount = models.IntegerField()
    size_range = models.CharField(max_length=30)
    cloth = models.CharField(max_length=30)
    quantity_in_line = models.IntegerField()
    material = models.CharField(max_length=30)
    checkbox_hit = models.BooleanField()
    checkbox_new = models.BooleanField(default=True)

    collection = models.ForeignKey(CollectionProducts, on_delete=models.CASCADE, related_name='products', null=True, blank=True)


    @property
    def get_images(self):
        images = ImageProducts.objects.filter(product=self)
        return [{'id': i.id, 'image': i.image.url} for i in images]


    def __str__(self):
        return self.title


class ImageProducts(models.Model):
    image = models.ImageField(upload_to='')
    color = ColorField(default='#FF0000')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

