from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
import logging
import os
from parser import parser

logger = logging.getLogger(__file__)
logger.debug("This logs a debug message.")
logger.info("This logs an info message.")
logger.warn("This logs a warning message.")
logger.error("This logs an error message.")

# Create your views here.
class Dashboard(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'dashboard/dashboard.html'

class Admin(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'dashboard/admin.html'

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('admin')

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('admin')

class BookDelete(DeleteView):
    model = Book
    context_object_name = 'books'
    template_name = 'dashboard/book_delete.html'
    success_url = reverse_lazy('admin')

class BookManipulationLog(ListView):
    model = CrudLog


def httpRequestLog(request):
    Logger.objects.all().delete()
    parser()

    logs = Logger.objects.all().order_by('-log')[:10]
    context = {'logs': logs}
    return render (request, 'dashboard/http-request-log.html', context)
