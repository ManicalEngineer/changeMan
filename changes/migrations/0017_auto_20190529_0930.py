# Generated by Django 2.2.1 on 2019-05-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changes', '0016_auto_20190525_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eco',
            name='priority',
            field=models.CharField(choices=[('1', 'High'), ('2', 'Medium'), ('3', 'Low')], default='1', max_length=3),
        ),
        migrations.AlterField(
            model_name='ecr',
            name='priority',
            field=models.CharField(choices=[('1', 'High'), ('2', 'Medium'), ('3', 'Low')], default='1', max_length=3),
        ),
    ]
