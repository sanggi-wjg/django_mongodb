# Django View
#### sample/stock/views.py
```
def detail(request, code):
    try:
        stock = Items.objects.get(code = code)
    except Items.DoesNotExist:
        raise Http404('Code does not exist')

    return render(
        request = request,
        template_name = 'stock/stock_detail.html',
        context = {
            'stock': stock
        },
    )
```
#### sample/sample/urls.py
```
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<str:code>', views.detail),
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
```

#### sample/sample/settings.py
```
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
STATICFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR), "static"),
    '/home/django_sample/static/',
]
```

#### static/comm/header.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <title>{% block view_title %}Django - DEV{% endblock %}</title>

    {% load static %}
    <link rel="icon" href="{% static 'comm/images/favicon.ico' %}">

    <script src={% static 'comm/js/jquery_3.4.1.js' %}></script>

</head>
<body>

{% block content %} {% endblock %}

</body>
</html>
```

#### static/comm/stock_detail.html
```
{% extends "comm/header.html" %}
{% block view_title %}{{ view_title }} {% endblock %}

{% block script_list %}
    {% load static %}

    <script>
        $(document).ready(function () {

        });
    </script>
{% endblock %}

{% block content %}

    {{ stock }}

{% endblock %}
```