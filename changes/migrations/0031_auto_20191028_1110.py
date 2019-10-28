# Generated by Django 2.2.1 on 2019-10-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changes', '0030_auto_20191024_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eco',
            name='priority',
            field=models.CharField(choices=[('3', 'Low'), ('1', 'High'), ('2', 'Medium')], default='1', max_length=3),
        ),
        migrations.AlterField(
            model_name='ecr',
            name='priority',
            field=models.CharField(choices=[('3', 'Low'), ('1', 'High'), ('2', 'Medium')], default='1', max_length=3),
        ),
    ]
