# Generated by Django 2.2.1 on 2019-06-06 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changes', '0020_auto_20190606_0820'),
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
