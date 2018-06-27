from django.urls import path
from .views import NoteCreate, NoteDelete, NoteUpdate, NoteDetail, NoteList
from .models import Note

urlpatterns = [
    path('', NoteList.as_view(), name='note-list'),
    path('<int:pk>/', NoteDetail.as_view(), name='note-detail'),
    path('add/', NoteCreate.as_view(), name='note-add'),
    path('<int:pk>/update/', NoteUpdate.as_view(), name='note-update'),
    path('<int:pk>/delete/', NoteDelete.as_view(), name='note-delete'),
]
