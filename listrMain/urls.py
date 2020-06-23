"""listrMain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from todo.views import todoView, addTodo, deleteTodo, moveTodo, finishTodo, deleteTodoFinal

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #SignUp System
    url('accounts/', include('accounts.urls')),
    #Login System
    url('accounts/', include('django.contrib.auth.urls')),
    url('^$', todoView),
    url('addTodo/', addTodo),
    url('deleteTodo/(?P<todo_id>\d+)/', deleteTodo),
    #add the url of MoveTodoItem here
    #finish moving the todo item
    url('moveTodo/(?P<todo_id>\d+)/', moveTodo),
    url('finishTodo/(?P<todo_id>\d+)/', finishTodo),
    url('deleteTodoFinal/(?P<todo_id>\d+)/', deleteTodoFinal),
    url('', TemplateView.as_view(template_name='home.html'), name='home')

]

urlpatterns += staticfiles_urlpatterns()
