# Generated by Django 3.0.4 on 2020-03-25 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_App', '0008_auto_20200325_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_attendance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='users_App.Profile'),
        ),
    ]
