from django.db import models


Sex = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]


class Position(models.Model):
    code = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=50)
    compensation = models.FloatField()
    duties = models.CharField(max_length=200)
    requirements = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Employee(models.Model):
    code = models.CharField(max_length=8, primary_key=True)
    fullname = models.CharField(max_length=30)
    birthday = models.DateField()
    sex = models.CharField(choices=Sex, max_length=20)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    person_id = models.CharField(max_length=20)
    position_code = models.ForeignKey(Position, to_field='code', on_delete=models.deletion.SET_NULL, null=True)

    def __str__(self):
        return self.fullname

    def say_my_code(self):
        return self.code


class AdvertisementType(models.Model):
    code = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Place(models.Model):
    code = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    type_code = models.ForeignKey(AdvertisementType, to_field='code', on_delete=models.deletion.SET_NULL, null=True)
    description = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.name
