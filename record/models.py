from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="标签名")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_date = models.DateTimeField(default=timezone.now, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "标签"


class Person(models.Model):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=100, verbose_name="姓名")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default=GENDER_CHOICE[0], verbose_name="性别")
    id_num = models.CharField(max_length=20, blank=True, null=True, verbose_name="身份证号")
    brief = models.CharField(max_length=1000, verbose_name="简要说明")
    # detail = models.CharField(max_length=10000, verbose_name="详细说明")
    detail = RichTextUploadingField()
    tag = models.ManyToManyField(Tag, blank=True, verbose_name="标签")
    visible = models.BooleanField(default=True, verbose_name="是否可见")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_date = models.DateTimeField(default=timezone.now, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "人员"


class AliasName(models.Model):
    name = models.CharField(max_length=100, verbose_name="别名")
    person = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="人员")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_date = models.DateTimeField(default=timezone.now, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "别名"


class Career(models.Model):
    name = models.CharField(max_length=100, verbose_name="职业行业")
    person = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="人员")
    primary_use = models.BooleanField(default=False, verbose_name="是否主要使用")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_date = models.DateTimeField(default=timezone.now, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "职业"


class Address(models.Model):
    name = models.CharField(max_length=1000, verbose_name="地址")
    person = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="人员")
    primary_use = models.BooleanField(default=False, verbose_name="是否主要使用")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_date = models.DateTimeField(default=timezone.now, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "地址"


class Phone(models.Model):
    num = models.CharField(max_length=20, verbose_name="电话号码")
    person = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="人员")
    primary_use = models.BooleanField(default=False, verbose_name="是否主要使用")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_date = models.DateTimeField(default=timezone.now, verbose_name="更新时间")

    def __str__(self):
        return self.num

    class Meta:
        verbose_name_plural = "电话号码"


class School(models.Model):
    name = models.CharField(max_length=100, verbose_name="学校名")
    person = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="人员")
    address = models.CharField(max_length=1000, blank=True, null=True, verbose_name="学校地址")
    primary_use = models.BooleanField(default=False, verbose_name="是否主要使用")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_date = models.DateTimeField(default=timezone.now, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "学校"


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name="公司名")
    person = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="人员")
    address = models.CharField(max_length=1000, blank=True, null=True, verbose_name="公司地址")
    primary_use = models.BooleanField(default=False, verbose_name="是否主要使用")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_date = models.DateTimeField(default=timezone.now, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "公司"


class QNum(models.Model):
    num = models.CharField(max_length=20, verbose_name="qq")
    person = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="人员")
    primary_use = models.BooleanField(default=False, verbose_name="是否主要使用")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_date = models.DateTimeField(default=timezone.now, verbose_name="更新时间")

    def __str__(self):
        return self.num

    class Meta:
        verbose_name_plural = "QQ"


class WeChat(models.Model):
    name = models.CharField(max_length=100, verbose_name="微信")
    person = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="人员")
    primary_use = models.BooleanField(default=False, verbose_name="是否主要使用")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_date = models.DateTimeField(default=timezone.now, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "微信"


class AliPay(models.Model):
    name = models.CharField(max_length=100, verbose_name="支付宝")
    person = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="人员")
    primary_use = models.BooleanField(default=False, verbose_name="是否主要使用")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_date = models.DateTimeField(default=timezone.now, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "支付宝"


class WeiBo(models.Model):
    name = models.CharField(max_length=100, verbose_name="微博")
    person = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="人员")
    primary_use = models.BooleanField(default=False, verbose_name="是否主要使用")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_date = models.DateTimeField(default=timezone.now, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "微博"


class Email(models.Model):
    name = models.CharField(max_length=100, verbose_name="邮件")
    person = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="人员")
    primary_use = models.BooleanField(default=False, verbose_name="是否主要使用")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_date = models.DateTimeField(default=timezone.now, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "邮件"


class Visitor(models.Model):
    ip = models.CharField(max_length=30)
    region = models.CharField(max_length=1000, blank=True, null=True)
    agent = models.CharField(max_length=1000)
    page = models.CharField(max_length=100)
    referer = models.CharField(max_length=500, blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    record_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)

    def increase_views(self):
        self.update_date = timezone.now()
        self.views += 1
        self.save(update_fields=['views', 'update_date'])
