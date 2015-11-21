# CRUD in Python and Django

This is a basic introduction to the Django Web Framework in Python. Django was developed in a newsroom, with deadlines in mind. As you get acquainted with it, it becomes obvious that it was built for a fast paced environment that requires rapid development with easy management and administration, security, and database toolsets. Django is fast and lightweight and follows many of the same conventions as frameworks like Rails. With that in mind, just about every core functionality you would want in a framework is available for import.


Let's get started:

1. Download the latest version of Python
2. brew install python (pip comes with HomeBrew)
3. pip install django
4. cd into directory
5. $ django-admin startproject MyNewProjectName
6. cd into project and atom .
7. $ python manage.py migrate
8. $ python manage.py runserver (you can change the port by declaring... $ python manage.py runserver 8080)
9. You have just created your first Python/ Django "project".  However, a project can have multiple apps, and
apps can belong to multiple projects. Now that we have the container for our project, lets create the app itself.
Make sure you are in the same directory as manage.py and type `python manage.py startapp NameOfApp`. The name is usually a plural noun, or the most basic description of what your app represents.  If you are building and survey app, then surveys.  If you are building a quiz, game, store, then proceed accordingly. This will contain your models, views, tests, and so on.
10. We will create a note-taking crud app, so 'Notes'.


### Create a Model
```
class Note(models.Model):
    title = models.ForeignKey(Title)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

```

These models in models.py will create the database schema and the access API for accessing the objects.


Now in settings.py add the models folder, in this case.. "notes" to:
```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notes',
)
```


### Migrations

Now that you have the model and the schema set up, you need to migrate the information. So now run the command
```
python manage.py makemigrations notes
```
running makemigrations tells your django app that you have made new changes to your models.

Now you can run
```
$ python manage.py migrate
```
to make the changes to the database.




Ultimately,
* Change your models (in models.py).
* Run python manage.py makemigrations to create migrations for those changes
* Run python manage.py migrate to apply those changes to the database.



### Admin

Django is big on management, in particular, the user-admin roles.  It is opinionated in the sense that you should
always create an admin user role to proceed, so that only admins can change and edit information. This is the site manager role.

To configure an admin role:

```
$ python manage.py createsuperuser

then enter your username

Username: admin

then email

Email address: admin@example.com

then password

Password: **********
Password (again): *********
Superuser created successfully.
```


### Server

Now you can run your local server and boot up your app.

```
$ python manage.py runserver
```

Go here and log in:

```
 http://127.0.0.1:8000/admin/
```

On a successful log in, you should see the admin dashboard.


There is a problem though, you do not see your app.  Go to admin.py and register your objects like this,
```
from django.contrib import admin
from .models import Note

admin.site.register(Note)
```


### Whoa... are you seeing what I'm seeing?

* That was pretty quick, and there are a lot of freebies here.  You now have full interactivity with your
standard SQL Lite DB and models.  Pretty awesome.

* The admin features at the reserved /admin are really useful, and there is plenty more you can do.  If you want to
learn more about customizing your admin dashboard [Go Here](https://docs.djangoproject.com/en/1.8/intro/tutorial02/).  But let's move on to the heart of the app.




### Views & URLS

Views in Django are like every other framework you have worked with.  Views are rendered after being called by a function that maps the URL pattern to its associated view.  In Django, they use 'URLConfs' which is just URL configuration in python.  To get a deeper understanding, [read this...](https://docs.djangoproject.com/en/1.8/topics/http/urls/)

Go to views.py and put this in:

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Django Unchained")
```
This is the index function that is, at least for now, going to render a string to the page.  But, we need to map this function to an actual URL so that we can access it.

If you don't already have a notes/urls.py ... create it.
So go to notes/urls.py and put this in:

```
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

```
You just imported the views to the URLS files and have used a regular expression to clean the url(in this case it is the 'index' so it reduces to '/'), are returning the string you provided, have named it the index so identify it for later.

Regular expressions are weird, and for the most part Django uses the same conventions over and over, so you will not have to write many custom Regexs. BUt, they're awesome and you should want to... get started by reading through this pretty well documented [wikipedia page.](https://en.wikipedia.org/wiki/Regular_expression)

Now go to YourAppName/urls.py and include this in the URL Patterns array:
```
url(r'^notes/', include('notes.urls'))

```

You are saying... when I go to the /notes path, use the associated view found in notes.urls.  Now check it out in the browser, voila.


Now lets say you want to add another route on top of the notes path and you want to be able to pass it a parameter like an Id.  Since we have already specified in our YourAppName/urls.py that anything in notes will be routed to /notes/  all we have to do is add another URL mapping in our notes/urls.py and another method inside of views.py.



urls.py
```
url(r'^(?P<note_id>[0-9]+)/$', views.detail, name='detail'),

```
The regular expression allows a number to be passed as the argument, and uses the detail method.

views.py
```
def detail(request, note_id):
    return HttpResponse("This is note %s." % note_id)

```

Detail takes a second argument, in this case the id we provide, and returns the HTTP response with the number that we have passed into the URL   /notes/SomeNumber.


Now go to the browser and check it out, it should change and update every time you pass it a new number.
Thats the basis of restful routing in Django.
