# Generated by Django 2.0.4 on 2018-05-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0005_auto_20180502_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateprofile',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
