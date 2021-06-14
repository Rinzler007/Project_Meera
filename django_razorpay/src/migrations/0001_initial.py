# Generated by Django 3.2.3 on 2021-05-22 17:14

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('contact_no', phonenumber_field.modelfields.PhoneNumberField(help_text='Add country code before the contact no.', max_length=128, region=None)),
                ('address_1', models.CharField(max_length=100, verbose_name='Address 1')),
                ('address_2', models.CharField(max_length=100, verbose_name='Address 2')),
                ('pincode', models.CharField(max_length=6, verbose_name='ZIP code')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('state', models.CharField(max_length=100, verbose_name='State')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
                ('order_id', models.CharField(blank=True, max_length=100)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
