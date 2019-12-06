from django.shortcuts import render,redirect
from django.db import models
from .models import Project,Message
from django.http import HttpResponse
from .forms import MessageModelForm,PostModelForm
from django.forms import modelformset_factory

# Create your views here.
def Home(request):
    return render(request, 'index.html')
def Blog(request):
    posted_projects = Project.objects.all
    return render(request, 'blog.html', {'posted_projects': posted_projects})
def Login(request):
    return render(request, 'login.html')
def Admin(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('/')
    else:
        form = PostModelForm()
    return render(request, 'admin.html',{'form': form})


def Forum(request, id_model):
    model_infos = Project.objects.get(id=id_model)
    posted_messages = Message.objects.all()
    if request.method == 'POST':
        msg = MessageModelForm(request.POST)
        if msg.is_valid():
            msg.message = request.POST.get("message")
            #PLACE FOR SAVING THE MESSAGE..
            post = msg.save()
            return redirect('/forum/' + str(model_infos.id))
    else:
        msg = MessageModelForm()
    return render(request, 'forum.html',{'form':msg,'posted_messages': posted_messages, 'model_infos': model_infos})
