# Generated by Django 5.0.1 on 2024-03-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patagonia', '0015_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
