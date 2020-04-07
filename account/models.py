from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from phone_field import PhoneField
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)

choices = [
    ("Male", "Male"),
    ('Female', 'Female')

]

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/', null=True, blank=True,help_text="Upload only .png, .jpg & .jpeg image extension.")
    phone = PhoneField(blank=True, help_text='Contact phone number')
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=choices)
    date_of_birth = models.DateField()
    address = models.TextField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.BigIntegerField()
    # current_user = models.IntegerField()

    class Meta:
        db_table = 'user_profile'
        verbose_name_plural = 'USER_PROFILE'
        managed = True

    def __str__(self):
        return str(self.user.id)


achoice = [

          ("Single Account", "Single Account"),
          ("Joint Account", "Joint Account")
      ]


class Account_details(models.Model):
    id = models.UUIDField(primary_key=True,	default=uuid4, editable = False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20, choices=achoice)
    balance = models.FloatField(default=0)
    date_of_opening = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'account_details'
        verbose_name_plural = 'ACCOUNT_DETAILS'
        managed = True

    def __str__(self):
        return str(self.id)


tchoice = [
        ('Online', 'Online'),
        ('Credit-Card', 'Credit Card')
    ]


class Transactions(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    Recipient_Name = models.CharField(max_length=110)
    transaction_type = models.CharField(max_length=110, choices=tchoice)
    amount = models.FloatField()
    account_no = models.PositiveIntegerField(
        unique=True,
        validators=[
            MinValueValidator(10000000),
            MaxValueValidator(99999999999999999)
        ]
    )
    IFSC= models.CharField(max_length=110)
    # date = models.DateTimeField(auto_now=True)
    current_user = models.IntegerField()

    class Meta:
        db_table = 'transaction'
        verbose_name_plural = 'TRANSACTION'
        managed = True

    def __str__(self):
        return str(self.id)


	
