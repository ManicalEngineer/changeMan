# Generated by Django 2.1.1 on 2019-05-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changes', '0015_auto_20190525_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eco',
            name='archive_status',
            field=models.CharField(blank=True, choices=[('CL', 'Complete'), ('IP', 'In Progress'), ('NA', 'Not Applicable')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eco',
            name='calcs_status',
            field=models.CharField(blank=True, choices=[('CL', 'Complete'), ('IP', 'In Progress'), ('NA', 'Not Applicable')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eco',
            name='drawings_status',
            field=models.CharField(blank=True, choices=[('CL', 'Complete'), ('IP', 'In Progress'), ('NA', 'Not Applicable')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eco',
            name='go_status',
            field=models.CharField(blank=True, choices=[('CL', 'Complete'), ('IP', 'In Progress'), ('NA', 'Not Applicable')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eco',
            name='jigs_status',
            field=models.CharField(blank=True, choices=[('CL', 'Complete'), ('IP', 'In Progress'), ('NA', 'Not Applicable')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eco',
            name='oa_status',
            field=models.CharField(choices=[('OH', 'On Hold'), ('CL', 'Complete'), ('IP', 'In Progress'), ('OP', 'Open'), ('CR', 'Created')], default='Created', max_length=30),
        ),
        migrations.AlterField(
            model_name='eco',
            name='part_status',
            field=models.CharField(blank=True, choices=[('CL', 'Complete'), ('IP', 'In Progress'), ('NA', 'Not Applicable')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eco',
            name='patterns_status',
            field=models.CharField(blank=True, choices=[('CL', 'Complete'), ('IP', 'In Progress'), ('NA', 'Not Applicable')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eco',
            name='priority',
            field=models.CharField(choices=[('2', 'Medium'), ('1', 'High'), ('3', 'Low')], default='1', max_length=3),
        ),
        migrations.AlterField(
            model_name='eco',
            name='test_status',
            field=models.CharField(blank=True, choices=[('CL', 'Complete'), ('IP', 'In Progress'), ('NA', 'Not Applicable')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ecr',
            name='priority',
            field=models.CharField(choices=[('2', 'Medium'), ('1', 'High'), ('3', 'Low')], default='1', max_length=3),
        ),
    ]
