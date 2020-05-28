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