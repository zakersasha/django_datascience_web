from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['event_name', 'title', 'full_text', 'question']

        widgets = {
            'event_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Событие'
            }),
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'question': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вопрос'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст для анализа'
            })
        }
