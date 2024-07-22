# Generated by Django 4.2.9 on 2024-01-11 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('people', models.IntegerField(default=10)),
            ],
        ),
    ]
