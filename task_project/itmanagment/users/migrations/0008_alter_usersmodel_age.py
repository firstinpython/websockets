# Generated by Django 5.1.3 on 2024-11-11 06:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_usersmodel_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersmodel',
            name='age',
            field=models.IntegerField(default=12, validators=[django.core.validators.MinValueValidator(0)], verbose_name='age'),
            preserve_default=False,
        ),
    ]
