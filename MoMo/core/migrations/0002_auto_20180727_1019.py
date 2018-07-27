# Generated by Django 2.0.7 on 2018-07-27 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentserviceprovider',
            name='slug',
        ),
        migrations.AddField(
            model_name='saasinstance',
            name='hostname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='saasinstance',
            name='address',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
