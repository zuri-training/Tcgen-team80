# Generated by Django 4.0.5 on 2022-08-10 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bussiness_name', models.CharField(max_length=23, null=True)),
                ('email_Address', models.CharField(max_length=23, null=True)),
                ('phone_number', models.CharField(max_length=23, null=True)),
                ('fax_number', models.CharField(max_length=23, null=True)),
                ('Address', models.CharField(max_length=23, null=True)),
                ('country', models.CharField(max_length=23, null=True)),
                ('state_province_or_teritory', models.CharField(max_length=23, null=True)),
                ('city', models.CharField(max_length=23, null=True)),
                ('zip_or_postal_code', models.CharField(max_length=23, null=True)),
            ],
        ),
    ]