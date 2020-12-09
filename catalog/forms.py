from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'text', 'price', 'currency', 'start_date', 'end_date', 'photo',)
        widgets = {
            'start_date': forms.DateInput(attrs={'placeholder': 'DD.MM.YYYY'}),
            'end_date': forms.DateInput(attrs={'placeholder': 'DD.MM.YYYY'}),
        }
        labels = {
            'title': 'Название курса',
            'text': 'Описание',
            'price': 'Стоимость',
            'currency': 'Валюта',
            'start_date': 'Дата начала курса',
            'end_date': 'Дата окончания',
            'photo': 'Изображение',

        }




class SearchForm(forms.Form):
    title = forms.CharField(max_length=50, required=False, label='Название курса')
    description = forms.CharField(max_length=50, required=False, label='Описание')
    start_date = forms.DateField(required=False, widget=forms.DateTimeInput(attrs={'placeholder': 'DD.MM.YYYY'}), label='Дата начала курса')
    start_date_is_greater_or_equal_to = forms.DateField(required=False, widget=forms.DateTimeInput(attrs={'placeholder': 'DD.MM.YYYY'}), label='Дата начала курса больше или равна')
    start_date_is_less_or_equal_to = forms.DateField(required=False, widget=forms.DateTimeInput(attrs={'placeholder': 'DD.MM.YYYY'}), label='Дата начала курса меньше или равна')




