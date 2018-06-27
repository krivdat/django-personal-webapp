from django.db import models
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(Category, default=4, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    hidden = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk})

    def hide(self):
        if self.hidden != True:
            self.hidden = True
            self.save()
            return "Switched to hidden"
        return "Already hidden"

    def unhide(self):
        if self.hidden == True:
            self.hidden = False
            self.save()
            return "Switched to visible"
        return "Already visible"

    def __str__(self):
        return self.title
