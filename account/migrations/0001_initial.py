# Generated by Django 3.0.5 on 2020-04-07 07:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, help_text='Upload only .png, .jpg & .jpeg image extension.', null=True, upload_to='images/')),
                ('contact', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('father_name', models.CharField(max_length=30)),
                ('mother_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.BigIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'USER_PROFILE',
                'db_table': 'user_profile',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Recipient_Name', models.CharField(max_length=110)),
                ('transaction_type', models.CharField(choices=[('Online', 'Online'), ('Credit-Card', 'Credit Card')], max_length=110)),
                ('amount', models.FloatField()),
                ('account_no', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999999999999)])),
                ('IFSC', models.CharField(max_length=110)),
                ('current_user', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'TRANSACTION',
                'db_table': 'transaction',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Account_details',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('account_type', models.CharField(max_length=20)),
                ('balance', models.FloatField(default=0)),
                ('date_of_opening', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'ACCOUNT_DETAILS',
                'db_table': 'account_details',
                'managed': True,
            },
        ),
    ]
