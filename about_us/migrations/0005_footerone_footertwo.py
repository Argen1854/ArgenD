# Generated by Django 4.0.4 on 2022-06-01 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0004_alter_helpimages_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('text', models.TextField()),
                ('number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FooterTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Number', 'Number'), ('Mail', 'Mail'), ('Instagram', 'Instagram'), ('Telegram', 'Telegram'), ('WhatsApp', 'WhatsApp')], max_length=100)),
                ('network', models.CharField(max_length=30)),
                ('link', models.TextField()),
            ],
        ),
    ]
