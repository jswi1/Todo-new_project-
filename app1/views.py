from django.shortcuts import render, redirect
from .models import *
from django.views import View

class todoView(View):
    def get(self, request):
        db = request.GET.get("qidirish")
        return render(request, 'todo.html', db)


def todo_ochir(request, son):
    Todo.objects.get(id=son).delete()
    return redirect(request, "/todo")