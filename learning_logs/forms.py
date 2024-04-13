from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        # 定制了字段‘text’的输入小部件，将文本宽度设置为80列，而不是默认的40列
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
    

