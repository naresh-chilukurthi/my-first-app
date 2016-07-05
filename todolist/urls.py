from django.conf.urls import url
from django.views.generic.edit import CreateView
from rest_framework.urlpatterns import format_suffix_patterns

from tododb import createitem
from todolist.crud import TodoListView, TodoView, DeleteList, CreateList, TodoListItemView
from . import views
urlpatterns = [
        url(r'^list/$',views.showlist),
url(r'^api/list/$',views.todo_list),
url(r'^api/list/(?P<pk>[0-9]+)/$',views.todo_detail),
url(r'^api/item/$',views.todo_item),
url(r'^api/item/(?P<pk>[A-Za-z0-9]+)/$',views.todo_item_detail),
url(r'^item/(?P<name>[A-Za-z0-9]+)/$',views.showitem),
url(r'^$',TodoListView.as_view(),name="home"),
url(r'^itemshow/(?P<name>[A-Za-z0-9]+)/$',TodoListItemView.as_view()),
url(r'^update/(?P<pk>[0-9]+)/$',TodoView.as_view()),
url(r'^delete/(?P<pk>[0-9]+)$',DeleteList.as_view()),
url(r'^create/$',CreateList.as_view())
        ]
urlpatterns = format_suffix_patterns(urlpatterns)