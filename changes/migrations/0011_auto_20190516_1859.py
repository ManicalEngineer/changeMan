# Generated by Django 2.1.1 on 2019-05-16 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changes', '0010_auto_20190515_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecr',
            name='close_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ecr',
            name='priority',
            field=models.CharField(choices=[('2', 'Medium'), ('1', 'High'), ('3', 'Low')], default='1', max_length=3),
        ),
        migrations.AlterField(
            model_name='eco',
            name='oa_status',
            field=models.CharField(choices=[('OH', 'On Hold'), ('CL', 'Closed'), ('IP', 'In Progress'), ('OP', 'Open'), ('CR', 'Created')], default='Created', max_length=30),
        ),
    ]
