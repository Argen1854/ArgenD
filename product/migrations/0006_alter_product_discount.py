# Generated by Django 4.0.4 on 2022-05-27 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_collectionproducts_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]