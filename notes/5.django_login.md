# Django Login
https://docs.djangoproject.com/en/3.0/topics/auth/default/
```
$ python manage.py startapp sign
```

## Backend
### sample/sample/settings.py
```
...

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

...

SIGNUP_URL = '/signup'
LOGIN_URL = '/login'
```

### sample/sign/views.py
```
class SignUpView(View):
    def get(self, request):
        return render(request, 'sign/signup.html', {
            'view_title': 'Signup',
            'user_form' : UserCreationForm()
        })

    def post(self, request):
        user_form = UserCreationForm(data = request.POST)

        if user_form.is_valid():
            user = user_form.save()
            print('USER_FORM:', user_form)
            print('USER:', user)
            authenticate(username = user.username, passowrd = user.password)

            return HttpResponseRedirect('/')

        else:
            return render(request, 'sign/signup.html', {
                'view_title': 'Signup',
                'user_form' : UserCreationForm(),
                'error'     : user_form.errors,
                'error_msg' : user_form.error_messages
            })
```
```
class LoginView(View):
    def get(self, request):
        return render(request, 'sign/login.html', {
            'view_title': 'Login',
            'login_form': AuthenticationForm()
        })

    def post(self, request):
        login_form = AuthenticationForm(request, request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect(settings.LOGIN_URL)

        else:
            return render(request, 'sign/login.html', {
                'view_title': 'Login',
                'login_form': AuthenticationForm(),
                'error_msg' : '다시!'
            })
```

```
class LogoutView(View):

    def get(self, request):
        logout(request)

        return HttpResponseRedirect(settings.LOGIN_URL)
```

## Route
### sample/sign/urls.py
```
from django.urls import path
from .views import SignUpView, LoginView, LogoutView, HomeView

urlpatterns = [
    path('', HomeView.as_view()),
    path('signup', SignUpView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
]
```

### sample/sample/urls.py
```
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('sign.urls')),
    path('stock/', include('stock.urls')),
]
```

## Html
### static/sign/login.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% load static %}
    <link rel="icon" href="{% static 'comm/images/favicon.ico' %}">
    <title>{{ view_title }}</title>
</head>
<body>
    {{ error_msg }}
    <form method="post">
        {% csrf_token %}
        {{ login_form }}
        <input type="submit">
    </form>
    <a href="/signup">회원가입</a>
</body>
</html>
```

## Html
### static/sign/signup.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    {% load static %}
    <link rel="icon" href="{% static 'comm/images/favicon.ico' %}">
    <title>{{ view_title }}</title>
</head>
<body>
    <form method="post">
        {% csrf_token %}
        {{ user_form }}
        <input type="submit">
    </form>

    {{ error }}
    {% for k, v in error_msg.items %}
        {{ k }} : {{ v }}
    {% endfor %}
</body>
</html>
```