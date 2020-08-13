from django.shortcuts import render
from django.http import HttpResponse
import yaml
import os

BASE_PATH = '/home/truongdt/Desktop/chatbot'
BASE_URL_API = 'http://localhost:5005'

# Create your views here.

def read_file(file_name):
    with open(file_name, 'r') as f:
        file_content = f.read()
    return file_content


def home(request):
    return render(request, 'home.html')

def status(request):
    import requests
    url_version = BASE_URL_API + '/version'
    url_status = BASE_URL_API + '/status'
    try:
        response = requests.request("GET", BASE_URL_API)
        status_code = response.status_code
        if status_code == 200:
            r_version = requests.request("GET", url_version)
            r_status = requests.request("GET", url_status)
            context = {"file_content": '\n'.join(('Server is online', r_version.text, r_status.text))}
        else:
            context = {"file_content": 'Server is offline'}
    except:
        context = {"file_content": 'Server is offline'}
    return render(request, 'status.html', context=context)

def config(request):
    file_name = 'config.yml'
    file_path = os.path.join(BASE_PATH, file_name)
    file_content = read_file(file_path)
    context = {
        'active_config': ' active',
        'file_content': file_content,
        'file_name': file_name
    }
    return render(request, 'content.html', context=context)


def nlu(request):
    file_name = 'nlu.md'
    file_path = os.path.join(BASE_PATH, 'data', file_name)
    file_content = read_file(file_path)
    context = {
        'active_nlu': ' active',
        'file_content': file_content,
        'file_name': file_name
    }
    return render(request, 'content.html', context=context)


def stories(request):
    file_name = 'stories.md'
    file_path = os.path.join(BASE_PATH, 'data', file_name)
    file_content = read_file(file_path)
    context = {
        'active_stories': ' active',
        'file_content': file_content,
        'file_name': file_name
    }
    return render(request, 'content.html', context=context)


def domain(request):
    file_name = 'domain.yml'
    file_path = os.path.join(BASE_PATH, file_name)
    file_content = read_file(file_path)
    context = {
        'active_domain': ' active',
        'file_content': file_content,
        'file_name': file_name
    }
    return render(request, 'content.html', context=context)


def credentials(request):
    file_name = 'credentials.yml'
    file_path = os.path.join(BASE_PATH, file_name)
    file_content = read_file(file_path)
    context = {
        'active_credentials': ' active',
        'file_content': file_content,
        'file_name': file_name
    }
    return render(request, 'content.html', context=context)


def endpoints(request):
    file_name = 'endpoints.yml'
    file_path = os.path.join(BASE_PATH, file_name)
    file_content = read_file(file_path)
    context = {
        'active_endpoints': ' active',
        'file_content': file_content,
        'file_name': file_name
    }
    return render(request, 'content.html', context=context)

from .models import Events, User
def tracker(request):
    events = Events.objects.all()
    context = {'active_tracker': ' active', 'events': events}
    return render(request, 'tracker.html', context=context)

from django.views import generic
from datetime import datetime
class EventsListView(generic.ListView):
    model = Events
    paginate_by = 10
    template_name = 'tracker.html'
    context_object_name = 'events'
    extra_context = {'active_tracker': 'active'}
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['active_tracker'] = 'active'
        context.update(self.extra_context)
        return context

class UserListView(generic.ListView):
    model = User
    paginate_by = 10
    template_name = 'data.html'
    context_object_name = 'users'
    extra_context = {'active_tracker': 'active'}
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['active_tracker'] = 'active'
        context.update(self.extra_context)
        return context

def training(request):
    from .models import Textuser
    textusers = Textuser.objects.all()
    context = {"text_users": textusers}
    print(type(textusers[0].intent_dict()))
    return render(request, 'training.html', context=context)