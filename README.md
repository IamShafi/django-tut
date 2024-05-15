## Lession 1
# pip install uv
```
C:\Users\shafi\AppData\Roaming\Python\Python312\Scripts\uv --version
C:\Users\shafi>C:\Users\shafi\AppData\Roaming\Python\Python312\Scripts\uv venv

```

# Run activate script
```
# On Windows. Set-ExecutionPolicy RemoteSigned

.venv\Scripts\activate
```

# Install Django
```
 C:\Users\shafi\AppData\Roaming\Python\Python312\Scripts\uv pip install Django
```

# start project
```
 django-admin startproject learnDjango 
 cd learnDjango
 ls
 python manage.py runserver 
 ```



 ## Lesson 2



 # Configuring the App
 ```
 INSTALLED_APPS = [
    ...
    'learnDjango',
]
```

# Creating Views and Templates, STATICFILES_DIRS in settings.py

```
views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! This is our first view.")
```

```
settings.py
Templates = [
    ...
    'DIRS': ['templates']
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```
# Routing URLs
```
urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

```

# Create a directory called templates


```
learnDjango
-> learnDjango
-> templates
```


# Starting the Server
```
ls
python manage.py runserver
```