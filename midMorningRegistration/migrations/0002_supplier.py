# Generated by Django 4.1.7 on 2023-03-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midMorningRegistration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sup_name', models.CharField(max_length=30)),
                ('sup_email', models.EmailField(max_length=30)),
                ('sup_phone', models.CharField(max_length=30)),
                ('sup_product', models.CharField(max_length=30)),
            ],
        ),
    ]
