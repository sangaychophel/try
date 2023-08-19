from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('aboutus', views.aboutus, name="aboutus"),
    path('registration', views.registration, name="registration"),
    path('contact', views.contact, name="contact"),
    path('login', views.login, name="login"),
    path('eventdetail', views.eventdetail, name="eventdetail"),
    path('insert',views.insertData, name="insertData"),
    path('insertdata',views.insertComment, name="insertComment"),
]