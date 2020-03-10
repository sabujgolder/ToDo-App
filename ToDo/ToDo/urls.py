from django.contrib import admin
from django.urls import path
from ToDoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('add',views.add_todo),
    path('delete/<int:id>/',views.delete_todo)
]
