# Django With MongoDB

Env Versions.
  - CentOS   7.8 
  - Python   3.8.3
  - Django   3.0.6
  - Docker   19.03
  - Maria DB 10.4
  - Mongo DB 

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
## Create Django Project
### Install Django
```
$ python -m pip install Django 
$ python -m django --version
```

### Create
