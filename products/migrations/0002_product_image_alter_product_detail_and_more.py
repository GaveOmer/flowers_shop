# Generated by Django 5.0.1 on 2024-01-29 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='Название продукта'),
        ),
    ]
