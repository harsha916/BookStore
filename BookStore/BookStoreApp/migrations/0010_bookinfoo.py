# Generated by Django 4.0.6 on 2022-07-24 16:27

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('BookStoreApp', '0009_bookinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfoo',
            fields=[
                ('bookname', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('bookprice', models.CharField(max_length=20)),
                ('bookurl', models.URLField()),
            ],
            managers=[
                ('variable', django.db.models.manager.Manager()),
            ],
        ),
    ]
