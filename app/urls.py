from . import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django_registration.backends.one_step.views import RegistrationView


from django.contrib.auth import views as auth_views
urlpatterns = [
    url('^$',views.index,name = 'index'),
    url('^edit_profile/(?P<username>\w{0,50})',views.edit_profile,name = 'edit_profile'),
    url('^businesses$',views.businesses,name = 'businesses'),
    url('^post/(?P<id>\d+)',views.post,name='post'),
    url(r'^search/$',views.search,name='search'),
    url('^api/businesses/$',views.BusinessList.as_view()),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # url(r'^logout/$', views.logout, {"next_page": '/'},name='logout'),
    url(r'^accounts/register/',RegistrationView.as_view(success_url='/accounts/login'),name='django_registration_register'),
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
   

]
