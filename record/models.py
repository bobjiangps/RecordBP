from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)


class Person(models.Model):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default=GENDER_CHOICE[0])
    id_num = models.CharField(max_length=20, blank=True, null=True)
    brief = models.CharField(max_length=1000)
    detail = models.CharField(max_length=10000)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    visible = models.BooleanField(default=True)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)


class AliasName(models.Model):
    name = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)


class Career(models.Model):
    name = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    primary_use = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)


class Address(models.Model):
    name = models.CharField(max_length=1000)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    primary_use = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)


class Phone(models.Model):
    num = models.CharField(max_length=20)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    primary_use = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)


class QNum(models.Model):
    num = models.CharField(max_length=20)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    primary_use = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)


class WeChat(models.Model):
    name = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    primary_use = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)


class AliPay(models.Model):
    name = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    primary_use = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)


class WeiBo(models.Model):
    name = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    primary_use = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)


class Email(models.Model):
    name = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    primary_use = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)
