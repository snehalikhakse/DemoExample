from django.urls import path
from Demoapp import views


urlpatterns = [
	path('',views.index2, name='index2'),

]