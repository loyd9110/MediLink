# Generated by Django 3.1.1 on 2023-05-16 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_remove_hospital_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitalservice',
            name='availability',
            field=models.BooleanField(default=False),
        ),
    ]