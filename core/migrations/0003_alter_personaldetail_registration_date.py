# Generated by Django 3.2 on 2021-04-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_personaldetail_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetail',
            name='registration_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
