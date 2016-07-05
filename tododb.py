import os
import click
import sys
import datetime
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "homeproject2.settings")
application = get_wsgi_application()
import todolist.models
@click.group()
def cli():
    pass
@cli.command()
def mange_user():
    click.echo("select your choice")
    click.echo("\n1.show lists\n2.delete lists\n3.create list")
    choice=click.prompt("",type=int)
    if choice==1:
        show_lists()
    elif choice==2:
        delete_lists()
    elif choice==3:
        populate()
    else:
        click.echo("wrong input")
        mange_user()

def show_lists():
    sl=todolist.models.Todolist.objects.all()
    for i in sl:
        print i.name,i.creation_date
    try:
        lname=click.prompt("enter list name to open it or enter 1 to add new list",type=str)
        if lname=='1':
            populate()
        else:
            show_items(lname)
    except Exception as e:
        print e
def show_items(name):
    print "in show_items func"
    si=todolist.models.Todoitem.objects.all().filter(owner=todolist.models.Todolist.objects.get(name=name))
    print si
    for i in si:
        print i.description,i.duedate,i.Completed
def delete_lists():
    todolist.models.Todolist.objects.all().delete()
    todolist.models.Todoitem.objects.all().delete()
def populate():
    name=click.prompt("enter name of todolist",type=str)
    creation_date=datetime.date.today()
    try:
        td=todolist.models.Todolist(name=name,creation_date=datetime.date.today())
        td.save()
    except Exception as e:
        print e

    createitem(name)
def createitem(list):
    desc=click.prompt("enter description of thing to do",type=str)
    try:
        year=click.prompt("enter year in YYYY",type=int)
        month = click.prompt("enter year in MM", type=int)
        day = click.prompt("enter year in DD", type=int)
        date1 = datetime.date(year, month, day)

        tl=todolist.models.Todoitem(description=desc,duedate=date1,Completed=False,owner=todolist.models.Todolist.objects.get(name=list))
        tl.save()
        choice=click.prompt("enter 1 to add more items or any int to exit",type=int)
        if choice==1:
            createitem(list)
    except Exception as e:
        print e
if __name__ == '__main__':
    cli()