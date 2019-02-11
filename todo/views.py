from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoModelForm

# Create your views here.
def list(request):
    todos = Todo.objects.all()
    return render(request, "todo/list.html", {"todos":todos})
    
def create(request):
    if request.method=="POST":
        form = TodoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todos:list")
    else:
        form = TodoModelForm()
    return render(request, "todo/create.html", {"form":form})

def detail(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, "todo/detail.html", {"todo":todo})
    
def update(request, id):
    todo = Todo.objects.get(id=id)
    if request.method=="POST":
        form = TodoModelForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todos:detail", id)
    else:
        form = TodoModelForm(instance=todo)
    return render(request, "todo/update.html", {"form":form})
    
def delete(request, id):
    todo = Todo.objects.get(pk=id)
    todo.delete()
    
    return redirect("todos:list")