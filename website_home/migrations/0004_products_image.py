# Generated by Django 3.2.3 on 2021-06-07 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_home', '0003_alter_products_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
