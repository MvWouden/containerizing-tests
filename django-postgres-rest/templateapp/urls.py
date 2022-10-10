from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from templateapp import views


urlpatterns = [
    path('todo/', views.todo_list),
    path('todo/<uuid:pk>', views.todo_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
