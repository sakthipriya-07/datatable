from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'contact', 'email'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
      }


from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'department', 'employee_cell_phone')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'department', 'employee_cell_phone')
