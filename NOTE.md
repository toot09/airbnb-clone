# Install pipenv
pip install pipenv

# Install virtual space (ver 3.X) : cd [Project dir]
pipenv --three (on Windows) 
pipenv --python 3.7 (on Mac)
 : In my case, 3.9 Didn't work on Mac

# Enter virtual space
pipenv shell

# Install Django (This project installed 2.2.5)
pipenv install Django==2.2.5

# Check complete install
django-admin

# Start Django project (Normal method)
django-admin startproject [project folder name]
# Start Django project (Efficient method)
1. django-admin startproject config
2. Move all files in config to root dir.
3. Delete Empty Folder named config

# Set time zone
Modify time setting [TIME_ZONE = "Asia/Seoul"] in "settings.py"

# Install python (In VSCode)
Install Python at Extensions menu.

# Install "Linter"

# Install formatting provider
pip install wheel
pip install black
pipenv install black --dev --pre

# Run Server
python manage.py(~.py) runserver

# Install app setting and create necessary database table
python manage.py(~.py) migrate

# Create SuperUser(administrator)
python manage.py(~.py) createsuperuser

# Create Apps(In this project that conversations, reviews, rooms ...)
django-admin startapp "appName"

# Information about Model field
https://docs.djangoproject.com/en/2.2/ref/models/fields/

# Install pillow for using ImageField (In this project Avatar Image)
pipenv install Pillow

# Install Django Countries Library
1. pipenv install django-countries
2. Add django_countries to INSTALLED_APPS(settings.py)

# Connect to the other models (below Example)
1. from users import models as user_models
2. host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

# Python functions (vars(), dir())
1. vars() : 모듈, 클래스, 인스턴스 또는 __dict__ 어트리뷰트가 있는 다른 객체의 __dict__ 어트리뷰트를 돌려줍니다.
2. dir() : 해당 객체에 유효한 어트리뷰트들의 리스트를 돌려주려고 시도합니다.
source (https://wikidocs.net/10307)

# Django Managers (https://docs.djangoproject.com/en/2.2/topics/db/managers/)
1. count() : [ex.) Room.objects.count()]
2. all() : [ex.) Room.objects.all()]
3. filter : [ex.) User.objects.filter(gender='male') / User.objects.filter(username__startswith='uj')]

# QuerySet (Important!)
url : https://docs.djangoproject.com/en/2.2/ref/models/querysets/

# Boolean return Def descript to "X" or "O" emoji
in_progress.boolean = True

# Def's Alias
in_progress.short_description = "PROGRESS"

# MEDIA_ROOT (config/setting.py)
Absolute filesystem path to the directory that will hold user-uploaded files.
Example: "/var/www/example.com/media/"
url : https://docs.djangoproject.com/en/2.2/ref/settings/
1. settings.py
 - MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")

# MEDIA_URL (config/setting.py)
RL that handles the media served from MEDIA_ROOT, used for managing stored files. It must end in a slash if set to a non-empty value. You will need to configure these files to be served in both development and production environments.
url : https://docs.djangoproject.com/en/2.2/ref/settings/
1. settings.py
 - MEDIA_URL = "/media/"
2. urls.py
 - from django.conf import settings
 - from django.conf.urls.static import static
 - if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    -> It means that settings.DEBUG==true is DEV. So It works on only DEV.
       In PRD set to url on Amazone S3.

# Set ImageField model's upload path
models.ImageField(upload_to="room_photos")

# MARK_SAFE : Allow HTML Tag
from django.utils.html import mark_safe
ex.) return mark_safe(f'<img width="100px" src="{obj.file.url}" />')

# InlineModelAdmin
Using admin into the other admin.
url : https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
1) Definite class 
class PhotoInline(admin.TabularInline):
    model = models.Photo
2) Definite inline in used model
inlines = (PhotoInline,)

# Install Django Snippets(Extension)
recommand Django expression

# Overriding Method
1) In Admin (Just executed on Admin)
def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
2) In Model (Executed Everywhere, Everytime when model modified)
def save(self, *args, **kwargs):
        do_something()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        do_something_else()

# Custom Django-admin Command
doc url : https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/
To do this, just add a management/commands directory to the application.

# Difference with *args and **args
1) *args : Tuple
2) **args : Dictionary

# Install Django-seed
1. pipenv install django_seed
2. Add django_seed to INSTALLED_APPS(settings.py)
** Reference : rooms/seed_rooms.py
3. Reference Faker : https://faker.readthedocs.io/en/master/index.html

# Calc date
Use datetime and timedelta
1) from datetime import datetime, timedelta
2) datetime.now()+timedelta(days=random.randint(3,25))

# template Setting
1) Make templates folder in root path
2) Setting templates path in settings
 - settings.py
 - TEMPLATES -> "DIRS": [os.path.join(BASE_DIR, "{My template folder}")],
3) Call template at views
     ex)
       from django.shortcuts import render
       def all_rooms(request):
       #return HttpResponse(content="hello")
       return render(request, "all_rooms.html")  

# Install Useful Extension for html and django
1) HTML Snippet
2) Django Template

# block (html)
 is like a window
# include
 is include other html (Such as header, footer, slide...)

# Get countries 
For example:
>>> from django_countries import countries
>>> dict(countries)['NZ']
'New Zealand'
>>> for code, name in list(countries)[:3]:
...     print(f"{name} ({code})")
...
Afghanistan (AF)
Åland Islands (AX)
Albania (AL)
reference : https://github.com/SmileyChris/django-countries#the-country-object