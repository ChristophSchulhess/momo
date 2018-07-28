# Generated by Django 2.0.7 on 2018-07-27 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180727_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='PspAdapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField()),
                ('psp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.PaymentServiceProvider')),
            ],
        ),
    ]