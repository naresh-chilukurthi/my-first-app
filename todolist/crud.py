from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView

from todolist.models import Todolist,Todoitem
class TodoListView(ListView):
   model=Todolist
   template_name = "todolist/todolist_list.html"
   context_object_name = "object_list"
    #  return reverse("/list")
class TodoView(UpdateView):
   model = Todolist
   template_name =  "todolist/update.html";
   fields=['name','creation_date']
   def get_success_url(self):
        return reverse('home')

class DeleteList(DeleteView):
    template_name = "todolist/delete.html"
    model=Todolist
    success_url = reverse_lazy('home')
class CreateList(CreateView):
    model=Todolist
    template_name = "todolist/create.html"
    fields = ['name','creation_date']
    success_url = reverse_lazy('home')
class TodoListItemView(ListView):
   model=Todoitem
   template_name = "todolist/todolist_item.html"
   context_object_name = "object_list"
   fields = ['name', 'duedate']

   def get(self, request, *args, **kwargs):
       return super(TodoListItemView, self).get(request, *args, **kwargs)

   def get_queryset(self):
       # location=self.kwargs.get('location')
       location = self.request.GET.get('name');
       if location:
           return Todoitem.objects.filter(owner=Todolist.objects.get(name=location))
       else:
           return super(TodoListItemView, self).get_queryset();