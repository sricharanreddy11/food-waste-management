# Generated by Django 4.2.9 on 2024-01-11 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_contribution_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contribution',
            name='phone',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
