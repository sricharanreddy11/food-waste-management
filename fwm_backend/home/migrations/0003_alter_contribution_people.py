# Generated by Django 4.2.9 on 2024-01-11 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_contribution_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='people',
            field=models.IntegerField(default=10),
        ),
    ]
