from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from templateapp.views import ToDoDetail, ToDoList


urlpatterns = [
    path('todo/', ToDoList.as_view()),
    path('todo/<uuid:pk>', ToDoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
