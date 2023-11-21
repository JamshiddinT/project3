# Generated by Django 4.2.6 on 2023-10-22 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_customuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('active', 'blocked')], default='active', max_length=20),
        ),
    ]
