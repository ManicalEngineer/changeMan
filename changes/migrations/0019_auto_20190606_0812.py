# Generated by Django 2.2.1 on 2019-06-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changes', '0018_auto_20190605_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eco',
            name='priority',
            field=models.CharField(choices=[('2', 'Medium'), ('1', 'High'), ('3', 'Low')], default='1', max_length=3),
        ),
        migrations.AlterField(
            model_name='ecr',
            name='priority',
            field=models.CharField(choices=[('2', 'Medium'), ('1', 'High'), ('3', 'Low')], default='1', max_length=3),
        ),
    ]
