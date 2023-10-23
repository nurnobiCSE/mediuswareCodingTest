from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *
urlpatterns = [    
    path('',UserLoginView.as_view(), name="login" ),
    path('registration/',RegistrationView.as_view() , name = "register"),
    path('home/',login_required(HomeView.as_view()),name='home'),
    path('taskdetails/<int:pk>/',login_required(TaskDetailView.as_view()),name='details'),
    path('updatetask/<int:pk>/', login_required(UpdateTaskView.as_view()), name='update'),
    path('delete/<int:pk>/',  login_required(DeleteTaskView.as_view()), name='delete'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
]