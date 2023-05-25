# Generated by Django 4.2.1 on 2023-05-25 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnterNewProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_purchase', models.DateField(auto_now=True)),
                ('supplier_of_goods', models.CharField(max_length=50)),
                ('invoice_number', models.CharField(max_length=15)),
                ('manufacturer', models.CharField(max_length=20)),
                ('product_category', models.CharField(max_length=20)),
                ('product_model', models.CharField(max_length=20)),
                ('quantity', models.CharField(max_length=4)),
                ('condition', models.CharField(choices=[('nau', 'nauja'), ('nuk', 'nukainuota')], max_length=15)),
                ('product_price', models.FloatField(max_length=15)),
            ],
        ),
    ]
