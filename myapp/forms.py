from django import forms
from myapp.models import Student, Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['label', 'favourite', 'image']

        widgets = {
            'label': forms.TextInput({'class': 'form-control'})
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password', 'school',
                  'city', 'interested_in', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'school': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'interested_in': forms.CheckboxSelectMultiple,
        }
