# Generated by Django 4.0.4 on 2022-06-06 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0001_initial'),
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
        migrations.AlterModelOptions(
            name='helpimages',
            options={'verbose_name': 'Помощь', 'verbose_name_plural': 'Помощь'},
        ),
        migrations.CreateModel(
            name='FooterTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Number', 'Number'), ('Mail', 'Mail'), ('Instagram', 'Instagram'), ('Telegram', 'Telegram'), ('WhatsApp', 'WhatsApp')], max_length=100)),
                ('network', models.CharField(max_length=30)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about_us.footerone')),
            ],
        ),
    ]