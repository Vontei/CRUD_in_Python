# Crud in Python and Django


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


```

```
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
