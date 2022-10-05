from django.urls import path
from templateapp import views


urlpatterns = [
    path('todo/', views.todo_list),
    path('todo/<uuid:pk>', views.todo_detail),
]
