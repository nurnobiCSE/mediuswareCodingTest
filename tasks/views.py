from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import  authenticate,login,logout
from .models import TaskModel
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

class UserLoginView(LoginView):
    def get(self,request):
        return render(request,'login.html')
    
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to your home page after a successful login
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
        

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('login')

class RegistrationView(View):
    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            message = "Username already exists. Please choose a different one."
            return render(request, 'registration.html', {'message': message})

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        user, created = User.objects.get_or_create(username=username, email=email)
        if created:
            user.set_password(password1)
            user.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Username or email already exists.')
            return redirect('register')

class HomeView(ListView):
    model = TaskModel
    template_name = 'index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter tasks by creation date
        creation_date = self.request.GET.get('creation_date')
        if creation_date:
            queryset = queryset.filter(creation_datetime__date=creation_date)

        # Filter tasks by due date
        due_date = self.request.GET.get('due_date')
        if due_date:
            queryset = queryset.filter(due_date__date=due_date)

        # Filter tasks by priority
        priority = self.request.GET.get('priority')
        if priority:
            queryset = queryset.filter(priority=priority)

        # Filter tasks by completion status
        is_complete = self.request.GET.get('is_complete')
        if is_complete:
            is_complete = is_complete.lower() == 'true'  # Convert to boolean
            queryset = queryset.filter(is_complete=is_complete)

        # Search for tasks by title
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(Q(title__icontains=title))

        return queryset

class TaskDetailView(DetailView):
    model = TaskModel
    template_name = 'taskDetails.html'
    context_object_name = 'task'    


class UpdateTaskView(UpdateView):
     model = TaskModel
     template_name = 'taskform.html'
     context_object_name = 'task'
     fields = ['title', 'description', 'due_date', 'priority', 'is_complete']  

     def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.object.pk})


class DeleteTaskView(DeleteView):
     model = TaskModel
     ontext_object_name = 'task'
     success_url = reverse_lazy('home')  # Redirect after successful deletion
     template_name = 'task_confirm_delete.html'