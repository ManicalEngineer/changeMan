# Generated by Django 2.2.1 on 2019-10-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0007_auto_20191024_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='part_description',
            field=models.CharField(max_length=100),
        ),
    ]
