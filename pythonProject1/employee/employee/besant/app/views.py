from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import employee

# Create your views here.

class employeeList(ListView):
    model = employee

class employeeDetail(DetailView):
    model = employee

class employeeCreate(CreateView):
    model = employee
    # Field must be same as the model attribute
    fields = ['name', 'identityNumber','address', 'department','age']
    success_url = reverse_lazy('employee_list')

class employeeUpdate(UpdateView):
    model = employee
    # Field must be same as the model attribute
    fields = ['name', 'identityNumber', 'address', 'department','age']
    success_url = reverse_lazy('employee_list')

class employeeDelete(DeleteView):
    model = employee
    success_url = reverse_lazy('employee_list')