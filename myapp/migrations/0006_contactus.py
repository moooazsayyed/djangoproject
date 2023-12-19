# Generated by Django 4.2.4 on 2023-10-03 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_listing_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(help_text='Enter phone number in format: +1234567890', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('messeage', models.CharField(max_length=500)),
            ],
        ),
    ]
