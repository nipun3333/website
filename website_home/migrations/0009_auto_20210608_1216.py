# Generated by Django 3.2.3 on 2021-06-08 06:46

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_home', '0008_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='cat_desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]