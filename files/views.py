from django.http import HttpResponse
from .models import Files
import os


def show_file_content(request, filename):
    user = request.user
    if user.is_authenticated:
        file_obj = Files.objects.filter(name=filename)
        if len(file_obj) > 0:
            current_file = file_obj[0]
            with open(os.path.join(current_file.path, filename), "r") as f:
                return HttpResponse(f'<pre>{current_file.content}</pre>')
        else:
            return HttpResponse("找不到文件")
    else:
        return HttpResponse("未登录")
