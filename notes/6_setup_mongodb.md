# MongoDB with Django

| Name | Ref |
| ------ | ------ |
| Tutorial | https://www.tutorialspoint.com/mongodb/index.htm |

### Overview

What is different between RDBMS and MongoDB?

| RDBMS | MongoDB |
| ------ | ------ |
| Database | Database |
| Table | Collection |
| Tuple/Row | Document |
| column | Field |
| Table Join | Embedded Documents |
| Primary Key | Primary Key (Default key _id provided by MongoDb) |

Data types which supports MongoDB.

| Type | Detail |
| ------ | ------ |
| String | This is the most commonly used datatype to store the data. String in MongoDB must be UTF-8 valid. |
| Integer  | This type is used to store a numerical value. Integer can be 32 bit or 64 bit depending upon your server. |
| Double  | This type is used to store floating point values. |
| Boolean  |  This type is used to store a boolean (true/ false) value. |
| Null  | This type is used to store a Null value. |
| Timestamp  | ctimestamp. This can be handy for recording when a document has been modified or added. |
| Min/ Max keys | This type is used to compare a value against the lowest and highest BSON elements. |
| Arrays  | This type is used to store arrays or list or multiple values into one key. |
| Object  | This datatype is used for embedded documents. |
| Symbol   | This datatype is used identically to a string; however, it's generally reserved for languages that use a specific symbol type. |
| Date   | This datatype is used to store the current date or time in UNIX time format. You can specify your own date time by creating object of Date and passing day, month, year into it. |
| Object ID  | This datatype is used to store the document’s ID. |
| Binary data  | This datatype is used to store binary data. |
| Code  | This datatype is used to store JavaScript code into the document. |
| Regular expression  | This datatype is used to store regular expression. |

#### Access MongoDB Container
```
$ docker exec -it mongo bash
```

#### Check Mongo
```
$ mongo -u root -p

> db.stats()
{
        "ok" : 0,
        "errmsg" : "command dbStats requires authentication",
        "code" : 13,
}

> db.help()
DB methods:
        db.adminCommand(nameOrDocument) - switches to 'admin' db, and runs command [just calls db.runCommand(...)]
        db.aggregate([pipeline], {options}) - performs a collectionless aggregation on this database; returns a cursor
        ...
        db.version() current version of the server
        db.watch() - opens a change stream cursor for a database to report on all  changes to its non-system collections.
```

#### Create Database
Input **"use [DATABASE_NAME]"** is used to create database. 
This command will create a new databases, if it doesn't exist, otherwise it will return the existing database.

Input **"[DATABASE_NAME]"** select database which you want to use.
```
> use backend
switched to db backend

> db 
backend
```

##### Insert sample data
```
> db.test.insert({"test":"111"})
WriteResult({ "nInserted" : 1 })

> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
test    0.000GB
```

##### Create Collection
```
> use backend
switched to db backend

> db.createCollection('finace_info')
{ "ok" : 1 }

> show collections
finance_info
```