from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from utils.geoip_helper import GeoIpHelper
from utils.yaml_helper import YamlHelper
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Visitor, Person
from .models import AliasName, Career, Address, Phone, QNum, WeChat, AliPay, WeiBo, Email, School, Company, Douyin, Xianyu, Baidu, OtherAccount
from django.contrib.auth import authenticate, login as d_login, logout as d_logout
import os

searched_person = None

def person_list_page(request):
    allow_list = YamlHelper.load_yaml(os.path.join(os.getcwd(), "config", "allow.yaml"))["person_list"]
    request.session['validate_error'] = False
    port = request.META.get("SERVER_PORT")
    if request.method == 'GET':
        user = request.user
        if user.is_authenticated:
            record_visit(request, page_suffix=f"/login=true&port={port}")
            person = Person.objects.filter(update_date__lte=timezone.now()).order_by('update_date').reverse()
            return pagination(request, person)
        else:
            record_visit(request, page_suffix=f"/login=false&port={port}")
            return render(request, 'record/identify.html')
    elif request.method == 'POST':
        id_num = request.POST["id-number"]
        if id_num in allow_list:
            record_visit(request, page_suffix=f"/verify=true&id={id_num}&port={port}")
            person = Person.objects.filter(update_date__lte=timezone.now()).order_by('update_date').reverse()
            return pagination(request, person)
        else:
            record_visit(request, page_suffix=f"/verify=false&id={id_num}&port={port}")
            request.session['validate_error'] = "错误身份信息"
            return render(request, 'record/identify.html')


def find_person_list_page(request):
    allow_list = YamlHelper.load_yaml(os.path.join(os.getcwd(), "config", "allow.yaml"))["person_list"]
    request.session['validate_error'] = False
    port = request.META.get("SERVER_PORT")
    user = request.user
    global searched_person
    if request.method == 'GET':
        if user.is_authenticated:
            record_visit(request, page_suffix=f"/login=true&port={port}")
            # if searched_person or request.get_full_path().find("?page=") > 0:
            if request.get_full_path().find("?page=") > 0:
                if searched_person:
                    return pagination(request, searched_person, num=100)
                else:
                    return render(request, 'record/identify_search.html')
            else:
                searched_person = None
                return render(request, 'record/identify_search.html')
        else:
            record_visit(request, page_suffix=f"/login=false&port={port}")
            return render(request, 'record/identify_search.html')
    elif request.method == 'POST':
        if user.is_authenticated:
            id_num = None
        else:
            id_num = request.POST["id-number"]
        keyword = request.POST["key-word"]
        if id_num in allow_list or user.is_authenticated:
            record_visit(request, page_suffix=f"/verify=true&id={id_num}&keyword={keyword}&port={port}")
            # person = Person.objects.filter(update_date__lte=timezone.now()).order_by('update_date').reverse()
            searched_person = get_person_object_by_keyword(keyword)
            return pagination(request, searched_person, num=100)
        else:
            record_visit(request, page_suffix=f"/verify=false&id={id_num}&keyword={keyword}&port={port}")
            request.session['validate_error'] = "错误身份信息"
            return render(request, 'record/identify_search.html')


def get_person_object_by_keyword(keyword):
    by_person_name = Person.objects.filter(name__contains=keyword)
    by_person_idnum = Person.objects.filter(id_num__contains=keyword)
    by_person_brief = Person.objects.filter(brief__contains=keyword)
    by_person_detail = Person.objects.filter(detail__contains=keyword)

    foreign_key_ids = []
    by_alias_name = AliasName.objects.filter(name__contains=keyword)
    if by_alias_name:
        for o in by_alias_name:
            foreign_key_ids.append(o.person.id)
    by_career_name = Career.objects.filter(name__contains=keyword)
    if by_career_name:
        for o in by_career_name:
            foreign_key_ids.append(o.person.id)
    by_address_name = Address.objects.filter(name__contains=keyword)
    if by_address_name:
        for o in by_address_name:
            foreign_key_ids.append(o.person.id)
    by_phone_num = Phone.objects.filter(num__contains=keyword)
    if by_phone_num:
        for o in by_phone_num:
            foreign_key_ids.append(o.person.id)
    by_school_name = School.objects.filter(name__contains=keyword)
    if by_school_name:
        for o in by_school_name:
            foreign_key_ids.append(o.person.id)
    by_company_name = Company.objects.filter(name__contains=keyword)
    if by_company_name:
        for o in by_company_name:
            foreign_key_ids.append(o.person.id)
    by_qq_num = QNum.objects.filter(num__contains=keyword)
    if by_qq_num:
        for o in by_qq_num:
            foreign_key_ids.append(o.person.id)
    by_wechat_name = WeChat.objects.filter(name__contains=keyword)
    if by_wechat_name:
        for o in by_wechat_name:
            foreign_key_ids.append(o.person.id)
    by_alipay_name = AliPay.objects.filter(name__contains=keyword)
    if by_alipay_name:
        for o in by_alipay_name:
            foreign_key_ids.append(o.person.id)
    by_weibo_name = WeiBo.objects.filter(name__contains=keyword)
    if by_weibo_name:
        for o in by_weibo_name:
            foreign_key_ids.append(o.person.id)
    by_email_name = Email.objects.filter(name__contains=keyword)
    if by_email_name:
        for o in by_email_name:
            foreign_key_ids.append(o.person.id)
    by_douyin_name = Douyin.objects.filter(name__contains=keyword)
    if by_douyin_name:
        for d in by_douyin_name:
            foreign_key_ids.append(d.person.id)
    by_xianyu_name = Xianyu.objects.filter(name__contains=keyword)
    if by_xianyu_name:
        for x in by_xianyu_name:
            foreign_key_ids.append(x.person.id)
    by_baidu_name = Baidu.objects.filter(name__contains=keyword)
    if by_baidu_name:
        for b in by_baidu_name:
            foreign_key_ids.append(b.person.id)
    by_other_account_name = OtherAccount.objects.filter(name__contains=keyword)
    if by_other_account_name:
        for oa in by_other_account_name:
            foreign_key_ids.append(oa.person.id)
    person_foreign = Person.objects.filter(id__in=foreign_key_ids)
    person = by_person_name | by_person_idnum | by_person_brief | by_person_detail | person_foreign
    return person


def person_detail_page(request, person_id):
    allow_list = YamlHelper.load_yaml(os.path.join(os.getcwd(), "config", "allow.yaml"))["person_detail"]
    request.session['validate_error'] = False
    port = request.META.get("SERVER_PORT")
    if request.method == 'GET':
        user = request.user
        if user.is_authenticated:
            record_visit(request, page_suffix=f"/login=true&port={port}")
            person = get_object_or_404(Person, pk=person_id)
            alias_name = AliasName.objects.filter(person=person_id)
            career = Career.objects.filter(person=person_id)
            address = Address.objects.filter(person=person_id)
            phone = Phone.objects.filter(person=person_id)
            school = School.objects.filter(person=person_id)
            company = Company.objects.filter(person=person_id)
            qq = QNum.objects.filter(person=person_id)
            wechat = WeChat.objects.filter(person=person_id)
            alipay = AliPay.objects.filter(person=person_id)
            weibo = WeiBo.objects.filter(person=person_id)
            email = Email.objects.filter(person=person_id)
            douyin = Douyin.objects.filter(person=person_id)
            xianyu = Xianyu.objects.filter(person=person_id)
            baidu = Baidu.objects.filter(person=person_id)
            other_account = OtherAccount.objects.filter(person=person_id)
            return render(request, 'record/person_detail.html', {'person': person,
                                                                 'alias_name': alias_name,
                                                                 'career': career,
                                                                 'address': address,
                                                                 'phone': phone,
                                                                 'school': school,
                                                                 'company': company,
                                                                 'qq': qq,
                                                                 'wechat': wechat,
                                                                 'alipay': alipay,
                                                                 'weibo': weibo,
                                                                 'email': email,
                                                                 'douyin': douyin,
                                                                 'xianyu': xianyu,
                                                                 'baidu': baidu,
                                                                 'other_account': other_account})
        else:
            record_visit(request, page_suffix=f"/login=false&port={port}")
            return render(request, 'record/identify_detail.html', {"person_id": person_id})
    elif request.method == 'POST':
        id_num = request.POST["id-number"]
        if id_num in allow_list:
            record_visit(request, page_suffix=f"/verify=true&id={id_num}&port={port}")
            person = get_object_or_404(Person, pk=person_id)
            alias_name = AliasName.objects.filter(person=person_id)
            career = Career.objects.filter(person=person_id)
            address = Address.objects.filter(person=person_id)
            phone = Phone.objects.filter(person=person_id)
            school = School.objects.filter(person=person_id)
            company = Company.objects.filter(person=person_id)
            qq = QNum.objects.filter(person=person_id)
            wechat = WeChat.objects.filter(person=person_id)
            alipay = AliPay.objects.filter(person=person_id)
            weibo = WeiBo.objects.filter(person=person_id)
            email = Email.objects.filter(person=person_id)
            douyin = Douyin.objects.filter(person=person_id)
            xianyu = Xianyu.objects.filter(person=person_id)
            baidu = Baidu.objects.filter(person=person_id)
            other_account = OtherAccount.objects.filter(person=person_id)
            return render(request, 'record/person_detail.html', {'person': person,
                                                                 'alias_name': alias_name,
                                                                 'career': career,
                                                                 'address': address,
                                                                 'phone': phone,
                                                                 'school': school,
                                                                 'company': company,
                                                                 'qq': qq,
                                                                 'wechat': wechat,
                                                                 'alipay': alipay,
                                                                 'weibo': weibo,
                                                                 'email': email,
                                                                 'douyin': douyin,
                                                                 'xianyu': xianyu,
                                                                 'baidu': baidu,
                                                                 'other_account': other_account})
        else:
            record_visit(request, page_suffix=f"/verify=false&id={id_num}&port={port}")
            request.session['validate_error'] = "错误身份信息"
            return render(request, 'record/identify_detail.html', {"person_id": person_id})


def pagination(request, filter_person, num=20):
    paginator = Paginator(filter_person, num)
    page = request.GET.get('page', 1)
    try:
        part_person = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page.
        part_person = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page of results
        part_person = paginator.page(paginator.num_pages)
    return render(request, 'record/person_list.html', {'person': part_person})


def do_login(request):
    port = request.META.get("SERVER_PORT")
    record_visit(request, page_suffix=f"/port={port}")
    if request.method == 'GET':
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
        request.session['login_error'] = False
        user = request.user
        if user.is_authenticated:
            return redirect(reverse("person_list"))
        else:
            return render(request, 'record/login.html')
    elif request.method == "POST":
        userName = request.POST['user-name']
        userPassword = request.POST['user-pw']
        user = authenticate(username=userName, password=userPassword)
        if user is not None:
            if user.is_active:
                d_login(request, user)
                # return redirect(request.session['login_from'])  # go back to page before login
                return redirect(reverse("person_list"))
            else:
                request.session['login_error'] = "未激活用户"
                return render(request,'record/login.html', {'username': userName,'password': userPassword})
        else:
            request.session['login_error'] = "错误的用户名或密码"
            return render(request,'record/login.html', {'username': userName,'password': userPassword})


def do_logout(request):
    port = request.META.get("SERVER_PORT")
    record_visit(request, page_suffix=f"/port={port}")
    d_logout(request)
    return redirect(reverse('person_list'))


def record_visit(request, page_suffix=""):
    try:
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            current_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        else:
            current_ip = request.META.get('REMOTE_ADDR')
        if "HTTP_USER_AGENT" in request.META:
            current_agent = request.META["HTTP_USER_AGENT"]
        else:
            current_agent = "no agent key in request"
        current_page = request.get_full_path() + page_suffix
        today = timezone.now()

        visitor_exist = Visitor.objects.filter(ip=str(current_ip), page=current_page, record_date__range=(today.date(), today.date() + timezone.timedelta(days=1)))
        if visitor_exist:
            current_visitor = visitor_exist[0]
            current_visitor.increase_views()
        else:
            current_visitor = Visitor()
            current_visitor.ip = current_ip
            ip_exist = Visitor.objects.filter(ip=str(current_ip)).order_by('-id')
            generate_new_location = True
            if ip_exist:
                generate_new_location = False
                temp_visitor = ip_exist[0]
                if (today - temp_visitor.record_date).days >= 7:
                    generate_new_location = True
                if temp_visitor.region:
                    current_visitor.region = temp_visitor.region
            if generate_new_location:
                if current_ip not in ["127.0.0.1", "localhost"]:
                    try:
                        current_visitor.region = GeoIpHelper.get_location(current_ip)
                    except Exception as e:
                        print("error when get location from ipify, message: %s" % str(e))
            current_visitor.agent = current_agent
            current_visitor.page = current_page
            if 'HTTP_REFERER' in request.META.keys():
                temp_referer = request.META["HTTP_REFERER"]
                temp_host = request.get_host()
                if temp_host not in temp_referer.split("/"):
                    current_visitor.referer = temp_referer
            current_visitor.record_date = today
            current_visitor.update_date = today
            current_visitor.views = 1
            current_visitor.save()
    except Exception as e:
        print("get error when record visitor, message: %s" % str(e))
        with open("./record_visitor_error.txt", "a") as f:
            f.write(str(timezone.now()))
            f.write("\n")
            f.write(str(e))
            f.write("\n\n")
