# Generated by Django 3.0.4 on 2020-03-25 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_App', '0006_auto_20200325_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_attendance',
            name='exit_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
