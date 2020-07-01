from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)


class AliasName(models.Model):
    name = models.CharField(max_length=100)


class Career(models.Model):
    name = models.CharField(max_length=100)


class Address(models.Model):
    name = models.CharField(max_length=1000)


class Phone(models.Model):
    num = models.CharField(max_length=20)


class QNum(models.Model):
    num = models.CharField(max_length=20)


class WeChat(models.Model):
    name = models.CharField(max_length=100)


class AliPay(models.Model):
    name = models.CharField(max_length=100)


class WeiBo(models.Model):
    name = models.CharField(max_length=100)


class Email(models.Model):
    name = models.CharField(max_length=100)


class Record(models.Model):
    VISIBLE_CHOICE = (
        ('0', 'public'),
        ('1', 'private')
    )
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default=GENDER_CHOICE[0])
    alias_name = models.ManyToManyField(AliasName, blank=True, null=True)
    career = models.ManyToManyField(Career, blank=True, null=True)
    address = models.ManyToManyField(Address, blank=True, null=True)
    id_num = models.CharField(max_length=20, blank=True, null=True)
    phone = models.ManyToManyField(Phone, blank=True, null=True)
    qq = models.ManyToManyField(QNum, blank=True, null=True)
    we_chat = models.ManyToManyField(WeChat, blank=True, null=True)
    ali_pay = models.ManyToManyField(AliPay, blank=True, null=True)
    wei_bo = models.ManyToManyField(WeiBo, blank=True, null=True)
    email = models.ManyToManyField(Email, blank=True, null=True)
    brief = models.CharField(max_length=1000)
    detail = models.CharField(max_length=10000)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    visible = models.CharField(max_length=10, choices=VISIBLE_CHOICE, default=VISIBLE_CHOICE[0])
