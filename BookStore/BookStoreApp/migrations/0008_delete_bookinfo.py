# Generated by Django 4.0.6 on 2022-07-24 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookStoreApp', '0007_bookinfo_delete_bookdetail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookInfo',
        ),
    ]