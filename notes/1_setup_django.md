### Create Project
```
$ django-admin startproject sample
```
That will create a directory **sample**.
```
sample - manage.py
       - sample    - asgi.py
                   - settings.py
                   - urls.py
                   - wsgi.py
```

##

### sample/sample/settings.py
> Before
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
> After
```
DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME'    : 'backend',
        'USER'    : 'root',
        'HOST'    : '127.0.0.1',
        'PASSWORD': 'wpdlwl',
        'PORT'    : '33061',
    }
}
```

##
### DB migrate
```
$ python manage.py makemigrations
$ python manage.py migrate
```
```
 MariaDB [backend]> show tables;
 +----------------------------+
 | Tables_in_backend          |
 +----------------------------+
 | auth_group                 |
 | auth_group_permissions     |
 | auth_permission            |
 | auth_user                  |
 | auth_user_groups           |
 | auth_user_user_permissions |
 | django_admin_log           |
 | django_content_type        |
 | django_migrations          |
 | django_session             |
 +----------------------------+
 10 rows in set (0.000 sec)
```
