# Generated by Django 4.0 on 2022-02-19 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_subscription_end_date_alter_subscription_start_date'),
        ('Stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('desc', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.account')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stores.product')),
            ],
        ),
    ]