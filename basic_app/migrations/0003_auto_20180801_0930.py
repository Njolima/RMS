# Generated by Django 2.0.7 on 2018-08-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20180730_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='Number',
            field=models.IntegerField(default=20, max_length=9),
        ),
    ]