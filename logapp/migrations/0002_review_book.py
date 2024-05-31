# Generated by Django 4.1.2 on 2022-11-18 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.BigIntegerField()),
                ('review', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logapp.customer')),
                ('mechanic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logapp.mechanic')),
            ],
            options={
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logapp.customer')),
                ('mechanic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logapp.mechanic')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
