# Generated by Django 5.0.1 on 2024-03-03 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patagonia', '0013_alter_portfolo_profileimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True)),
                ('h1_title', models.CharField(max_length=150)),
                ('meta_description', models.CharField(max_length=200)),
                ('published', models.CharField(max_length=90)),
                ('blogimage', models.ImageField(upload_to='static/images')),
            ],
        ),
    ]
