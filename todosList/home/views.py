from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDos

# Create your views here.
def todosTask(request):
    # return HttpResponse("This is tasks page")
    tasks = ToDos.objects.all()
    context = {'tasks':tasks}
    return render(request, 'home/tasks.html', context)

def todosAddTask(request):
    # return HttpResponse("This is add task page")
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        ins = ToDos(taskTitle=title, taskDesc=desc)
        ins.save()
        return redirect('tasks')

    return render(request, 'home/addTask.html')

def todosUpdateTask(request, pk):
    task = ToDos.objects.get(id=pk)
    title = task.taskTitle
    desc = task.taskDesc
    context = {'title': title, 'desc': desc}
    if request.method == 'POST':
        newTitle = request.POST.get('title')
        newDesc = request.POST.get('desc')
        task.taskTitle = newTitle
        task.taskDesc = newDesc
        task.save()
        return redirect('tasks')

    return render(request, 'home/updateTask.html', context)

def todosDeleteTask(request, pk):
    item = ToDos.objects.get(id=pk)
    item.delete()
    return redirect('/')