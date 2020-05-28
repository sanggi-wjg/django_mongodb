### Install Docker
```
$ yum install docker docker-registry

$ systemctl enable docker
$ systemctl start docker

$ systemctl status docker 
```

### Setup Docker
Download MariaDB image
```
$ docker pull mariadb:10.4
$ docker pull mongo:4.2.7

$ docker image ls
```

Launching MariaDB (Not recommended for production) 
```
$ docker run -d -p 33061:3306 -e MYSQL_ROOT_PASSWORD=wpdlwl --name maria mariadb:10.4
$ docker run -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=wpdlwl --name mongo mongo:4.2.7

$ docker ps -a
```

To use a separate data volume for /var/lib/mysql (recommended, to allow image update without losing database contents)

Create a data volume container: (it doesn't matter what image you use here, we'll never run this container again; it's just here to reference the data volume)
```
$ docker run --name=maria-data -v /var/lib/mysql <yourname>/mariadb true
$ docker run --name=maria -d -p 3306:3306 --volumes-from=mariadb-data -e MYSQL_ROOT_PASSWORD=<password> <yourname>/mariadb
```


Setup MariaDB
```
$ docker exec -it maria bash

$ mysql -u root -p

MariaDB > CREATE SCHEMA `backend` DEFAULT CHARACTER SET utf8;
MariaDB > exit;

$ exit
```