"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from .views import ListTaskView, ListTagView, DetailTaskView, DetailTagView, AddTaskView, AddTagView

urlpatterns = [
    path('tasks/', ListTaskView.as_view(), name="tasks-all"),
    path('tags/', ListTagView.as_view(), name="tags-all"),
    path('tasks/<int:pk>', DetailTaskView.as_view(), name="task-specific"),
    path('tags/<int:pk>', DetailTagView.as_view(), name="tag-specific"),
    path('tasks/create', AddTaskView.as_view(), name="task-addition"),
    path('tags/create', AddTagView.as_view(), name="tag-addition"),
]
