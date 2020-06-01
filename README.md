# Django With MongoDB
Env Versions.

| Name | Version |
| ------ | ------ |
| CentOS | 7.8  |
| Python | 3.8.3 |
| Django | 3.0.6 |
| Docker | 1.13 |
| MariaDB | 10.4 |
| MongoDB | 4.2.7 |

### Install pyenv
```
$ yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel git gcc openssl-devel libffi-devel bzip2-devel wget

$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```
```
$ vi ~/.bashrc

# INSERT BELOW
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

$ source ~/.bashrc
```

### Create Python 3.8 ENV using pyenv
```
Check available python versions before develop.
$ pyenv install --list | grep -v - |tail

Install python 3.8.3
$ pyenv install 3.8.3
$ pyenv versions

$ mkdir /home/django_sample
$ cd /home/django_sample

$ pyenv local 3.8.3
$ pip install --upgrade pip
$ pip install virtualenv

$ virtualenv dm_venv
$ source dm_venv/bin/activate
(When want stop, $ deactivate)
```
#
### Django
```
$ python -m pip install Django
$ python -m django --version
```

### Before Start Django
Install Docker and create MariaDB, MongoDB Container.

See the install_docker.md for more information.

[install_docker.md](https://github.com/sanggi-wjg/django_mongodb/blob/master/notes/0_install_docker.md)

### Dependencies
```
$ yum install mariadb-devel
$ pip install mysqlclient
```

## Notes

| Name | Ref |
| ------ | ------ |
| Setup Django | [Setup Django](https://github.com/sanggi-wjg/django_mongodb/blob/master/notes/1_setup_django.md) |
| App | [Django App](https://github.com/sanggi-wjg/django_mongodb/blob/master/notes/2_django_app.md) |
| Model | [Django Model](https://github.com/sanggi-wjg/django_mongodb/blob/master/notes/3_django_model.md) |
| Pycharm | Pycharm sets the HTML file auto-complete code or label for Django templates http://www.programmersought.com/article/790273239/ |
| View  | [Django View](https://github.com/sanggi-wjg/django_mongodb/blob/master/notes/4_django_view.md) |
| Signup, Login  | [Django Signup, Login](https://github.com/sanggi-wjg/django_mongodb/blob/master/notes/4_django_view.md) |
