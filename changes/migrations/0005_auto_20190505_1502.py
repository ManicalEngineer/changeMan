# Generated by Django 2.1.1 on 2019-05-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changes', '0004_auto_20190505_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecr',
            name='ecr_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ecr',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
