# Generated by Django 2.2.1 on 2019-06-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changes', '0024_auto_20190606_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eco',
            name='priority',
            field=models.CharField(choices=[('3', 'Low'), ('2', 'Medium'), ('1', 'High')], default='1', max_length=3),
        ),
        migrations.AlterField(
            model_name='ecr',
            name='impact',
            field=models.CharField(blank=True, default='N/A', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ecr',
            name='priority',
            field=models.CharField(choices=[('3', 'Low'), ('2', 'Medium'), ('1', 'High')], default='1', max_length=3),
        ),
        migrations.AlterField(
            model_name='ecr',
            name='remediation',
            field=models.CharField(blank=True, default='N/A', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ecr',
            name='requested_change',
            field=models.CharField(blank=True, default='N/A', max_length=300, null=True, verbose_name='Requested Change or Improvement'),
        ),
        migrations.AlterField(
            model_name='ecr',
            name='requirements',
            field=models.CharField(blank=True, default='N/A', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ecr',
            name='solution',
            field=models.CharField(blank=True, default='N/A', max_length=300, null=True, verbose_name='Solution & Cost'),
        ),
        migrations.AlterField(
            model_name='ecr',
            name='steps',
            field=models.CharField(blank=True, default='N/A', max_length=300, null=True),
        ),
    ]
