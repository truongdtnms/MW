from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('config', views.config, name='config'),
    path('nlu', views.nlu, name='nlu'),
    path('stories', views.stories, name='stories'),
    path('domain', views.domain, name='domain'),
    path('credentials', views.credentials, name='credentials'),
    path('endpoints', views.endpoints, name='endpoints'),
    path('tracker', views.EventsListView.as_view(), name='tracker'),
    path('member', views.UserListView.as_view(), name='member'),
    path('status', views.status, name='status'),
    path('training', views.training, name='training'),
    path('intent', views.intent, name='intent')
]
