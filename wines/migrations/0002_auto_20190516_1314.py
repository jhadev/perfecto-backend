# Generated by Django 2.2.1 on 2019-05-16 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='vintage',
            field=models.IntegerField(),
        ),
    ]
