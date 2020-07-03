# Generated by Django 3.0.8 on 2020-07-03 20:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20200703_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='address',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='address',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='record.Person', verbose_name='人员'),
        ),
        migrations.AlterField(
            model_name='address',
            name='primary_use',
            field=models.BooleanField(default=False, verbose_name='是否主要使用'),
        ),
        migrations.AlterField(
            model_name='address',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='aliasname',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='aliasname',
            name='name',
            field=models.CharField(max_length=100, verbose_name='别名'),
        ),
        migrations.AlterField(
            model_name='aliasname',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='record.Person', verbose_name='人员'),
        ),
        migrations.AlterField(
            model_name='aliasname',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='alipay',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='alipay',
            name='name',
            field=models.CharField(max_length=100, verbose_name='支付宝'),
        ),
        migrations.AlterField(
            model_name='alipay',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='record.Person', verbose_name='人员'),
        ),
        migrations.AlterField(
            model_name='alipay',
            name='primary_use',
            field=models.BooleanField(default=False, verbose_name='是否主要使用'),
        ),
        migrations.AlterField(
            model_name='alipay',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='career',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='career',
            name='name',
            field=models.CharField(max_length=100, verbose_name='职业行业'),
        ),
        migrations.AlterField(
            model_name='career',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='record.Person', verbose_name='人员'),
        ),
        migrations.AlterField(
            model_name='career',
            name='primary_use',
            field=models.BooleanField(default=False, verbose_name='是否主要使用'),
        ),
        migrations.AlterField(
            model_name='career',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='公司地址'),
        ),
        migrations.AlterField(
            model_name='company',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100, verbose_name='公司名'),
        ),
        migrations.AlterField(
            model_name='company',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='record.Person', verbose_name='人员'),
        ),
        migrations.AlterField(
            model_name='company',
            name='primary_use',
            field=models.BooleanField(default=False, verbose_name='是否主要使用'),
        ),
        migrations.AlterField(
            model_name='company',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='email',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='email',
            name='name',
            field=models.CharField(max_length=100, verbose_name='邮件'),
        ),
        migrations.AlterField(
            model_name='email',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='record.Person', verbose_name='人员'),
        ),
        migrations.AlterField(
            model_name='email',
            name='primary_use',
            field=models.BooleanField(default=False, verbose_name='是否主要使用'),
        ),
        migrations.AlterField(
            model_name='email',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='person',
            name='brief',
            field=models.CharField(max_length=1000, verbose_name='简要说明'),
        ),
        migrations.AlterField(
            model_name='person',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='person',
            name='detail',
            field=models.CharField(max_length=10000, verbose_name='详细说明'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=('M', 'Male'), max_length=10, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='person',
            name='id_num',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='身份证号'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=100, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='person',
            name='tag',
            field=models.ManyToManyField(blank=True, to='record.Tag', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='person',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='person',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='是否可见'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='num',
            field=models.CharField(max_length=20, verbose_name='电话号码'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='record.Person', verbose_name='人员'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='primary_use',
            field=models.BooleanField(default=False, verbose_name='是否主要使用'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='qnum',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='qnum',
            name='num',
            field=models.CharField(max_length=20, verbose_name='qq'),
        ),
        migrations.AlterField(
            model_name='qnum',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='record.Person', verbose_name='人员'),
        ),
        migrations.AlterField(
            model_name='qnum',
            name='primary_use',
            field=models.BooleanField(default=False, verbose_name='是否主要使用'),
        ),
        migrations.AlterField(
            model_name='qnum',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='school',
            name='address',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='学校地址'),
        ),
        migrations.AlterField(
            model_name='school',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=100, verbose_name='学校名'),
        ),
        migrations.AlterField(
            model_name='school',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='record.Person', verbose_name='人员'),
        ),
        migrations.AlterField(
            model_name='school',
            name='primary_use',
            field=models.BooleanField(default=False, verbose_name='是否主要使用'),
        ),
        migrations.AlterField(
            model_name='school',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, verbose_name='标签名'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='wechat',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='wechat',
            name='name',
            field=models.CharField(max_length=100, verbose_name='微信'),
        ),
        migrations.AlterField(
            model_name='wechat',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='record.Person', verbose_name='人员'),
        ),
        migrations.AlterField(
            model_name='wechat',
            name='primary_use',
            field=models.BooleanField(default=False, verbose_name='是否主要使用'),
        ),
        migrations.AlterField(
            model_name='wechat',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='weibo',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='weibo',
            name='name',
            field=models.CharField(max_length=100, verbose_name='微博'),
        ),
        migrations.AlterField(
            model_name='weibo',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='record.Person', verbose_name='人员'),
        ),
        migrations.AlterField(
            model_name='weibo',
            name='primary_use',
            field=models.BooleanField(default=False, verbose_name='是否主要使用'),
        ),
        migrations.AlterField(
            model_name='weibo',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
    ]
