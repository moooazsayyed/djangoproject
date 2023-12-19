# Generated by Django 4.2.4 on 2023-10-02 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_posting_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='listings/')),
                ('description', models.CharField(max_length=500)),
                ('lost_and_found', models.BooleanField(default=False)),
                ('categorie', models.CharField(choices=[('mobile', 'Mobile'), ('people', 'People'), ('pets', 'Pets')], max_length=50)),
                ('state', models.CharField(choices=[('andhra_pradesh', 'Andhra Pradesh'), ('arunachal_pradesh', 'Arunachal Pradesh'), ('assam', 'Assam'), ('bihar', 'Bihar'), ('chhattisgarh', 'Chhattisgarh'), ('goa', 'Goa'), ('gujarat', 'Gujarat'), ('haryana', 'Haryana'), ('himachal_pradesh', 'Himachal Pradesh'), ('jammu_kashmir', 'Jammu and Kashmir'), ('jharkhand', 'Jharkhand'), ('karnataka', 'Karnataka'), ('kerala', 'Kerala'), ('madhya_pradesh', 'Madhya Pradesh'), ('maharashtra', 'Maharashtra'), ('manipur', 'Manipur'), ('meghalaya', 'Meghalaya'), ('mizoram', 'Mizoram'), ('nagaland', 'Nagaland'), ('odisha', 'Odisha'), ('punjab', 'Punjab'), ('rajasthan', 'Rajasthan'), ('sikkim', 'Sikkim'), ('tamil_nadu', 'Tamil Nadu'), ('telangana', 'Telangana'), ('tripura', 'Tripura'), ('uttar_pradesh', 'Uttar Pradesh'), ('uttarakhand', 'Uttarakhand'), ('west_bengal', 'West Bengal'), ('andaman_nicobar', 'Andaman and Nicobar Islands'), ('chandigarh', 'Chandigarh'), ('dadra_nagar_haveli', 'Dadra and Nagar Haveli'), ('daman_diu', 'Daman and Diu'), ('delhi', 'Delhi'), ('lakshadweep', 'Lakshadweep'), ('puducherry', 'Puducherry')], max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(help_text='Enter phone number in format: +1234567890', max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Posting',
        ),
    ]
