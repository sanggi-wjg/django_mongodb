# Django App 

#### create app folder
```
$ python manage.py startapp stock
```
That will create a directory **stock**.
```
stock - mirgations 
      - admin.py
      - apps.py
      - models.py
      - tests.py
      - views.py
```

## Hello Django!
###  sample/settings.py
Add address.
```
ALLOWED_HOSTS = [
    '192.168.10.6',
]
```

Add apps created **stock**.
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'stock',
]
```

### sample/urls.py
Add route.
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('stock/', include('stock.urls'))
]
```

### sample/urls.py
Create a file **urls.py** in app directory.
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
]
```
index
```
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello Django')
```

## Launching Django app!
```
$ python manage.py runserver 0:8000
```
If you can't connect, you have to open port on server.
```
$ firewall-cmd --permanent --zone=public --add-port=8000/tcp
$ firewall-cmd --reload
```