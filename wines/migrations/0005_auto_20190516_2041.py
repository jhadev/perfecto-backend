# Generated by Django 2.2.1 on 2019-05-17 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0004_auto_20190516_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='case_price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='wine',
            name='vintage',
            field=models.IntegerField(choices=[(2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], default=2015),
        ),
    ]
