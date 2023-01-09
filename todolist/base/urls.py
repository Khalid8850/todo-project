from django.urls import path
from .import views as v
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login',v.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',v.RegisterPage.as_view(), name='register'),

    path('',v.TaskList.as_view(),name='task'),
    path('taskdtl/<int:pk>',v.TaskDetail.as_view(),name='taskdtl'),
    path('create-form',v.TaskCreate.as_view(),name='create-form'),
    path('edit-task/<int:pk>',v.UpdateTask.as_view(),name='edit-task'),
    path('delete-task/<int:pk>',v.DeleteTask.as_view(),name='delete-task')
]