from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    title = models.CharField(max_length=20)
    text = RichTextField()


    @property
    def get_images(self):
        image = AboutImages.objects.filter(about = self)
        return [{'id': i.id, 'image': i.image.url} for i in image]


class AboutImages(models.Model):
    image = models.ImageField(upload_to='')

    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_image')
    

class Benefits(models.Model):
    images = models.ImageField(upload_to='')

    title = models.CharField(max_length=50)
    text = models.TextField()


class News(models.Model):
    images = models.ImageField(upload_to='')

    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.title


class HelpImages(models.Model):
    image = models.ImageField(upload_to='')


class Help(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

    
class Offer(models.Model):
    title = models.CharField(max_length=50)
    text = RichTextField()

    def __str__(self):
        return self.title