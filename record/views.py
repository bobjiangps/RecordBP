from django.shortcuts import render


def main_page(request):
    # port = request.META.get("SERVER_PORT")
    # record_visit(request, page_suffix=f"/port={port}")
    return render(request, 'record/main.html')
