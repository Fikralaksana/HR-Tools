# Generated by Django 3.2.5 on 2021-07-12 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_employee_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='age',
        ),
        migrations.AddField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to='photo_profil'),
        ),
    ]
