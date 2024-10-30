from django.urls import path
from. import views
urlpatterns = [
    path('',views.demo),
    path('demo/',views.demo,name="demo")
]
