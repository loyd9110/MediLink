# Generated by Django 3.1.1 on 2023-05-16 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]