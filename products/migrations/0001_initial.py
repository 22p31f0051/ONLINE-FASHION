# Generated by Django 3.2 on 2023-11-14 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('price', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 11, 14, 14, 50, 18, 677259))),
            ],
        ),
    ]
