from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *
urlpatterns = [    
    path('task/',login_required(TaskApiView.as_view()), name="taskapi" ),
    
]