# Generated by Django 3.1.1 on 2022-10-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_user_pay_per_day1_user_sick_leave_user_tax_rate1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tax_rate1',
        ),
        migrations.AddField(
            model_name='user',
            name='tax_rate',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pay_per_day1',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
