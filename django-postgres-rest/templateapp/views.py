from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from templateapp.models import ToDo
from templateapp.serializers import ToDoSerializer


class ToDoList(ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoDetail(RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
