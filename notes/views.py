from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note


class NoteList(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'my_notes'
    def get_queryset(self):
        if 
        return Note.objects.filter(author=self.request.user)


class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = [
        'title',
        'text',
        'category',
        'hidden',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = [
        'author',
        'title',
        'text',
        'category',
        'hidden',
    ]


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
