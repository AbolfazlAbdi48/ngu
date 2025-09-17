from django import forms
from .models import DurabilityTest

class DurabilityTestForm(forms.ModelForm):
    class Meta:
        model = DurabilityTest
        fields = ['user_name','user_phone','user_industry', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14']
        widgets = {
            'user_name':forms.TextInput(attrs={'required': True, 'type': 'tel', 'placeholder':'نام و نام خانوادگی'}),
            'user_phone':forms.TextInput(attrs={'required': True, 'type': 'tel', 'placeholder': 'شماره تلفن'}),
            'user_industry':forms.TextInput(attrs={'required': True, 'type': 'tel', 'placeholder':'حوزه فعالیت'}),
            'q1': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'q2': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'q3': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'q4': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'q5': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'q6': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'q7': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'q8': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'q9': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'q10': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'q11': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'q12': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'q13': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'q14': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
        }