# Generated by Django 4.2.9 on 2024-01-30 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_contribution_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='requests',
            field=models.IntegerField(default=0),
        ),
    ]
