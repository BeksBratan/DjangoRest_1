# Generated by Django 4.0.1 on 2022-01-12 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopBackend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='ShopBackend.Tag'),
        ),
    ]