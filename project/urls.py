from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth import views



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'',include('app.urls')),

]
