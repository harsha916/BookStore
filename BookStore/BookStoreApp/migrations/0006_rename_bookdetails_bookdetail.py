# Generated by Django 4.0.6 on 2022-07-24 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookStoreApp', '0005_rename_bookdetail_bookdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookDetails',
            new_name='BookDetail',
        ),
    ]