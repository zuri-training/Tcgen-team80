# Generated by Django 4.0.5 on 2022-08-10 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('termsgen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='database',
            old_name='Bussiness_name',
            new_name='Company_name',
        ),
    ]