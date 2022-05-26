from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    title = models.CharField(max_length=20)
    text = RichTextField()


    @property
    def get_images(self):
        image = AboutImages.objects.filter(about = self)
        return [{'id': i.id, 'image': i.image.url} for i in image]


    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class AboutImages(models.Model):
    image = models.ImageField(upload_to='')

    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_image')
    

class Benefits(models.Model):
    images = models.ImageField(upload_to='')

    title = models.CharField(max_length=50)
    text = models.TextField()


    class Meta:
        verbose_name = 'Наши преимущества'
        verbose_name_plural = 'Наши преимущества'


class News(models.Model):
    images = models.ImageField(upload_to='')

    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class HelpImages(models.Model):
    image = models.ImageField(upload_to='')


    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Помощь изображение'


class Help(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

    
    class Meta:
        verbose_name = 'Помощь'
        verbose_name_plural = 'Помощь'

    
class Offer(models.Model):
    title = models.CharField(max_length=50)
    text = RichTextField()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Публичная оферта'
        verbose_name_plural = 'Публичная оферта'