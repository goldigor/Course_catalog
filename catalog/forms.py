from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'text', 'price', 'currency', 'start_date', 'end_date', 'photo',)




class SearchForm(forms.Form):
    title = forms.CharField(max_length=50, required=False)
    description = forms.CharField(max_length=50, required=False)
    start_date = forms.DateField(required=False)
    start_date_is_greater_or_equal_to = forms.DateField(required=False)
    start_date_is_less_or_equal_to = forms.DateField(required=False)




