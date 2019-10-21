from django.urls import path
from . import views


app_name = 'CV'  # here for namespacing of urls.

urlpatterns = [
    path("", views.cv, name="cv" )
]