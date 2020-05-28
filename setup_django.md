### Create Project
```
$ django-admin startproject sample
```
##

#### sample/sample/settings.py
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

