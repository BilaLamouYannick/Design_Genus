# Generated by Django 4.0 on 2022-01-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_remove_account_is_premium'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]
