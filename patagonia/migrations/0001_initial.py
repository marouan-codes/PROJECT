# Generated by Django 5.0.1 on 2024-01-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h1_tag', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=200)),
                ('duree', models.CharField(max_length=40)),
                ('designtool', models.ImageField(upload_to='static/images')),
                ('devtool', models.ImageField(upload_to='static/images')),
                ('siteimages', models.ImageField(upload_to='static/images')),
                ('text_info', models.CharField(max_length=1000)),
            ],
        ),
    ]
