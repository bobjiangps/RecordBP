from django.contrib import admin
from .models import Tag, AliasName, Career, Address, Phone, QNum, WeChat, AliPay, WeiBo, Email, Person, School, Company, Douyin, Xianyu

admin.site.register(Tag)
admin.site.register(Person)
admin.site.register(AliasName)
admin.site.register(Career)
admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(QNum)
admin.site.register(WeChat)
admin.site.register(WeiBo)
admin.site.register(AliPay)
admin.site.register(Email)
admin.site.register(School)
admin.site.register(Company)
admin.site.register(Douyin)
admin.site.register(Xianyu)
