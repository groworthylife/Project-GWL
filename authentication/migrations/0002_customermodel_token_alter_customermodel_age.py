# Generated by Django 4.2 on 2023-04-08 17:01

import authentication.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermodel',
            name='token',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='age',
            field=models.IntegerField(default=18, validators=[authentication.validators.validate_age]),
        ),
    ]