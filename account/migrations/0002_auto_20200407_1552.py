# Generated by Django 3.0.4 on 2020-04-07 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account_details',
            old_name='User_account_no',
            new_name='account_no',
        ),
    ]
