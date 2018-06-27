from django import forms

from .models import Note

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('title', 'text', 'category',)
        
    def add_note(self):
        # store new note using the self.cleaned_data dictionary
        pass
        