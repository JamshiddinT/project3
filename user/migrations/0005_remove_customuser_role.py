# Generated by Django 4.2.6 on 2023-10-22 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_customuser_date_joined_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='role',
        ),
    ]
