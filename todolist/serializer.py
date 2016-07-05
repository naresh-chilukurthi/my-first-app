from rest_framework import serializers
from todolist.models import Todolist, Todoitem


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = ('id', 'name', 'creation_date')
class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todoitem
        fields = ('description', 'duedate', 'Completed','owner')