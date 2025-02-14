from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Choose category')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), empty_label='Choose  status')
    
    
    class Meta:
        model = Task
        fields =[
            'name',
            'description',
            'category',
            'status',
        ]
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
        labels = {
            'name': 'Create category', 
        }