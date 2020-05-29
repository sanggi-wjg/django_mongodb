# Django Model
### sample/stock/models.py
```
from django.db import models

class Items(models.Model):
    code = models.CharField(max_length = 10)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return '{} {}'.format(self.code, self.name)

```

### sample/sample/settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'stock.apps.StockConfig',
]
```

Django migration
```
$ python manage.py makemigrations stock

Migrations for 'stock':
  stock/migrations/0001_initial.py
    - Create model Items
```

```
$ python manage.py sqlmigrate stock 0001

--
-- Create model Items
--
CREATE TABLE `stock_items` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `code` varchar(10) NOT NULL, `name` varchar(100) NOT NULL);
```

```
python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, stock
Running migrations:
  Applying stock.0001_initial... OK
```

### Before develop using model, install django-debug-toolbar for debug.
https://django-debug-toolbar.readthedocs.io/en/latest/tips.html#the-toolbar-isn-t-displayed
```
$ pip install django-debug-toolbar
```

#### sample/sample/settings.py
``` 
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
```
then
``` 
$ python manage.py collectstatic
```

#### sample/sample/settings.py
``` 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'stock.apps.StockConfig',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1', 'ADD_IP_ADDRESS'] 
``` 

#### sample/sample/urls.py
``` 
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stock/', include('stock.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
``` 