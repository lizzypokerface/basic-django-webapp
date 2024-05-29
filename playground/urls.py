from django.urls import path
from . import views

# URLConf - playground/hello/
urlpatterns = [path("hello/", views.say_hello)]  # say_hello is a function reference
