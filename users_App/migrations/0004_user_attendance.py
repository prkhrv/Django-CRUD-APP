# Generated by Django 3.0.4 on 2020-03-25 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_App', '0003_auto_20200324_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present', models.BooleanField(default=False)),
                ('present_time', models.DateTimeField(auto_now_add=True)),
                ('exit_time', models.DateTimeField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_App.Profile')),
            ],
        ),
    ]
