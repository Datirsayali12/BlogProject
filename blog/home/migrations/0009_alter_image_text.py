# Generated by Django 4.2.7 on 2023-12-27 18:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_image_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
