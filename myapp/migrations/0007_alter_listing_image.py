# Generated by Django 4.2.4 on 2023-10-03 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.cmss.gov.in%2Fgoverning-body%2F&psig=AOvVaw2Ghh0fc_OSZbjB5p8PvfSJ&ust=1696328331081000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLi-v8-R14EDFQAAAAAdAAAAABAJ', upload_to='media/listings/images'),
        ),
    ]
