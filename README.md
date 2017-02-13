# wishlist
A book wishlist REST API built with Django

## Installation
Clone the repo
cd into the repo directory
create a clean Python3 virtual environment and activate it
```
$ python3 -m virtualenv ./
$ . bin/activate
```

Install requirements:
```
$ pip install -r requirements.txt
```

Make migrations, Migrate, and create a super user:
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```

Run the test server:
```
$ python manage.py runserver
```

## Commands: GET, POST, DELETE

## Endpoints: /book/, /book/<pk>/, /users/, /users/<pk>/

## Usage
Either open a browser to the sever url
or
Use command line requests to server
```
$ http -a usrname:password --form POST http://127.0.0.1:8000/book/ title="Foo" author="Bar"
```
