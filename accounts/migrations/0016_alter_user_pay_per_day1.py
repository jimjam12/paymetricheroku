# Generated by Django 4.1.3 on 2022-11-11 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_attendance_id_alter_requestleave_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pay_per_day1',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]