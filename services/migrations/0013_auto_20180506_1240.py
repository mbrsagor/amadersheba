# Generated by Django 2.0.4 on 2018-05-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_auto_20180506_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='condition',
            field=models.CharField(choices=[('family', 'Family'), ('bachelor', 'Bachelor')], max_length=10),
        ),
    ]
