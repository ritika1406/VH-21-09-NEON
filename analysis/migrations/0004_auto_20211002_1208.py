# Generated by Django 3.2.6 on 2021-10-02 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_rename_hospital_name_patient_status_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulance',
            name='address_link',
            field=models.CharField(default='abc', max_length=700),
        ),
        migrations.AddField(
            model_name='beds',
            name='address_link',
            field=models.CharField(default='abc', max_length=700),
        ),
        migrations.AddField(
            model_name='icu_beds',
            name='address_link',
            field=models.CharField(default='abc', max_length=700),
        ),
        migrations.AddField(
            model_name='oxygen',
            name='address_link',
            field=models.CharField(default='abc', max_length=700),
        ),
        migrations.AddField(
            model_name='plasma',
            name='address_link',
            field=models.CharField(default='abc', max_length=700),
        ),
        migrations.AddField(
            model_name='vaccination',
            name='address_link',
            field=models.CharField(default='abc', max_length=700),
        ),
    ]
