# Generated by Django 2.2.1 on 2019-06-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changes', '0022_auto_20190606_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eco',
            name='priority',
            field=models.CharField(choices=[('1', 'High'), ('2', 'Medium'), ('3', 'Low')], default='1', max_length=3),
        ),
        migrations.AlterField(
            model_name='ecr',
            name='part_numbers',
            field=models.ManyToManyField(blank=True, null=True, to='parts.Part', verbose_name='Affected Part Numbers'),
        ),
        migrations.AlterField(
            model_name='ecr',
            name='priority',
            field=models.CharField(choices=[('1', 'High'), ('2', 'Medium'), ('3', 'Low')], default='1', max_length=3),
        ),
    ]
