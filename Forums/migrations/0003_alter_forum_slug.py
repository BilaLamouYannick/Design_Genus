# Generated by Django 4.0 on 2022-03-12 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forums', '0002_alter_forum_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]