# Generated by Django 3.2.6 on 2021-11-04 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]
