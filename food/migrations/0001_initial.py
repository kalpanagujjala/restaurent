# Generated by Django 5.0 on 2024-07-30 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='res',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veg', models.CharField(max_length=20)),
                ('nonveg', models.CharField(max_length=20)),
            ],
        ),
    ]
