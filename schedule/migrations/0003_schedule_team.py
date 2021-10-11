# Generated by Django 3.2.7 on 2021-09-27 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210924_1723'),
        ('schedule', '0002_schedule_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.team', verbose_name='チーム'),
        ),
    ]