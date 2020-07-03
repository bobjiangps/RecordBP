from django.shortcuts import render
from django.utils import timezone
from utils.geoip_helper import GeoIpHelper
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Visitor, Person


def main_page(request):
    allowed_id = ["ProtectAnimal"]
    request.session['validate_error'] = False
    port = request.META.get("SERVER_PORT")
    if request.method == 'GET':
        record_visit(request, page_suffix=f"/port={port}")
        return render(request, 'record/main.html')
    elif request.method == 'POST':
        id_num = request.POST["id-number"]
        if id_num in allowed_id:
            record_visit(request, page_suffix=f"/verify=true&id={id_num}&port={port}")
            person = Person.objects.filter(update_date__lte=timezone.now()).order_by('update_date').reverse()
            return pagination(request, person)
        else:
            record_visit(request, page_suffix=f"/verify=false&id={id_num}&port={port}")
            request.session['validate_error'] = "错误身份信息"
            return render(request, 'record/main.html')


def pagination(request, filter_person):
    paginator = Paginator(filter_person, 20)
    page = request.GET.get('page', 1)
    try:
        part_person = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page.
        part_person = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page of results
        part_person = paginator.page(paginator.num_pages)
    return render(request, 'record/main.html', {'person': part_person})


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
