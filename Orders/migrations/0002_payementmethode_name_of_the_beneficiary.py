# Generated by Django 4.0 on 2022-03-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payementmethode',
            name='name_of_the_beneficiary',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
