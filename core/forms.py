from django import forms
from .models import Students

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ("name", "roll", "city")
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control shadow'}),
            'roll': forms.NumberInput(attrs={'class':'form-control shadow'}),
            'city': forms.TextInput(attrs={'class':'form-control shadow'}),
        }