# Generated by Django 2.2.1 on 2019-06-06 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0003_auto_20190606_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='part_description',
            field=models.CharField(max_length=40),
        ),
    ]
