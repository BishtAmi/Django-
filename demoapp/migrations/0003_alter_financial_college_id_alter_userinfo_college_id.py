# Generated by Django 4.1.13 on 2024-03-18 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_financial_alter_userinfo_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financial',
            name='college_id',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='college_id',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
