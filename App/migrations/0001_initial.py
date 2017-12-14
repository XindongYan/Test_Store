# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detailed_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('UserName', models.CharField(max_length=100)),
                ('Image', models.FileField(upload_to='/Detailed_list')),
                ('Store_Name', models.CharField(max_length=100)),
                ('Unit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('images', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Shopping_Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Image', models.FileField(upload_to='Shopping_Cart/')),
                ('Store_Name', models.CharField(max_length=100)),
                ('Unit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('New_Store', models.CharField(max_length=100)),
                ('Unit', models.IntegerField()),
                ('Images', models.FileField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=1000)),
            ],
        ),
    ]
