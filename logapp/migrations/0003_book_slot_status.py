# Generated by Django 4.1.2 on 2022-11-18 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0002_review_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slot_status',
            field=models.CharField(default='pending', max_length=150),
        ),
    ]
