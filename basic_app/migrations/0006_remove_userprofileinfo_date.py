# Generated by Django 2.0.7 on 2018-08-02 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_userprofileinfo_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='date',
        ),
    ]
