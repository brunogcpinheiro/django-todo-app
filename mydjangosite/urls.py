"""mydjangosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from todo.views import todo_view, add_todo, delete_todo, done_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_view),
    path('add_todo/', add_todo),
    path('delete_todo/<int:todo_id>/', delete_todo),
    path('done_todo/<int:todo_id>/', done_todo),
]
