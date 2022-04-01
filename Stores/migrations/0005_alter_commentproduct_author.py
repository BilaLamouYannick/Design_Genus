# Generated by Django 4.0 on 2022-02-23 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_subscription_end_date_alter_subscription_start_date'),
        ('Stores', '0004_alter_commentproduct_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentproduct',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.account'),
        ),
    ]
