from django.urls import path

from todo import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('loginn/', views.loginn, name = 'loginn'),
    path('todopage/', views.todo, name = 'todopage'),
    path('edit_todo/<int:srno>/', views.edit_todo, name='edit_todo'),
    path('delete_todo/<int:srno>/', views.delete_todo, name='delete_todo'),
    path('signout/', views.signout, name='signout')
]
