import pathlib
from django.shortcuts import render
from visits.models import PageVisit

from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "my page"
    my_context = {
        "page_title": my_title,
        "queryset": page_qs,
        "page_visit_count": page_qs.count(),
        "percent":(page_qs.count() *100.0)/ qs.count(),
        "total_visit_count":qs.count()
    }
    path = request.path
    print("path", path)

    html_template = "home.html"
    PageVisit.objects.create(path=request.path)

    return render(
        request,
        html_template,
        my_context,
    )


def old_home_page_view(request, *args, **kwargs):
    my_title = "my page"
    my_context = {
        "page_title": my_title,
    }
    html_ = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>{page_title} is anything</h1>
</body>
</html>
""".format(
        **my_context
    )

    return HttpResponse(html_)
