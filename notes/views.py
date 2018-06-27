from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Note


class NoteList(ListView):
    model = Note
    context_object_name = 'my_notes'

class NoteDetail(DetailView):
    model = Note
                    
class NoteCreate(CreateView):
    model = Note
    fields = [
        'author',
        'title',
        'text',
        'category',
        'hidden',
    ]

class NoteUpdate(UpdateView):
    model = Note
    fields = [
        'author',
        'title',
        'text',
        'category',
        'hidden',
    ]

class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
