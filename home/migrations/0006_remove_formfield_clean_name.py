# Generated by Django 2.2.16 on 2020-09-08 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_formfield_clean_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formfield',
            name='clean_name',
        ),
    ]
