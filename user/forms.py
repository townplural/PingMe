from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistrationForm(UserCreationForm):
    
    """
    
    def clean_email
    Сначала получается email введённый пользователем 
    Идёт проверка 
    
    CustomUser.objects.filter(email=email)
    Ищутся все объекты модели CustomUser, у которых поле email равно значению переменной email, возвращается QuerySet
    
    exclude(id=self.instance.id)
    Фильтрует QuerySet исключая объекты соответствующие условию(id=self.instance.id)
    self.instance - текущий объект с которым работает форма
    
    .exists() - Проверяет есть ли в бд объект, который соответствует тому, что написано до
    Если есть совпадение, то вернётся True
    
    """
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'username': '',
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Данный email уже зарегистрирован')
        return email


class EditUserForm(forms.ModelForm):
    
    """
    profile_picture - не обязательное поле, т.к. не всем нужно фото
    
    """
    
    profile_picture = forms.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = ['profile_picture', 'username', 'first_name', 'last_name']
        
class ProfileUserForm(forms.ModelForm):
    
    """
    exclude исключаем telegram_confirmation_code, дабы у пользователя всё работало коректно
    
    """
    
    class Meta:
        model = CustomUser
        exclude = ['telegram_confirmation_code', ]
        

