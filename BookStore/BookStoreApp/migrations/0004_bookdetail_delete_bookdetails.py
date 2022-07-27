# Generated by Django 4.0.6 on 2022-07-24 09:53

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('BookStoreApp', '0003_bookdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookDetail',
            fields=[
                ('bookname', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('bookprice', models.CharField(max_length=20)),
            ],
            managers=[
                ('variable', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='BookDetails',
        ),
    ]
