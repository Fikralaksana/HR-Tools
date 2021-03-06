# Generated by Django 3.2.5 on 2021-07-11 04:44

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_contract'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.TextField(max_length=500)),
                ('contract_start', models.DateTimeField()),
                ('contract_end', models.DateTimeField(blank=True)),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.TextField(max_length=1000)),
                ('contract_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.contract')),
            ],
        ),
    ]
