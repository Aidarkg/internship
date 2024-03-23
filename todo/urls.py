from django.contrib import admin
from django.urls import path
from aidar.views import TaskDetailAPIView, TaskListAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', TaskListAPIView.as_view(), name='task_list'),
    path('task/<int:id>/', TaskDetailAPIView.as_view(), name='task_detail'),
]
