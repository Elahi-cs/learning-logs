from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'public']
        labels = {'text': '', 'public': 'Public '}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'public']
        labels = {'text': '', 'public': 'Public'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        