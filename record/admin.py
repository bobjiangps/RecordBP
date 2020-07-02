from django.contrib import admin
from .models import Tag, AliasName, Career, Address, Phone, QNum, WeChat, AliPay, WeiBo, Email, Person

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
