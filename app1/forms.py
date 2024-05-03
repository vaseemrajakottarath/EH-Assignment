from django import forms
from .models import Helper,Customer

class HelperForm(forms.ModelForm):
    class Meta:
        model = Helper
        fields = ['name', 'gender', 'age','skills']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['skills'].widget.attrs['class'] = 'checkbox-group required'

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        name = cleaned_data.get('name')
        age = cleaned_data.get('age')
        gender = cleaned_data.get('gender')

        # skills = cleaned_data.get('skills')
        skills = cleaned_data.get('skills')

        print("SKILLS IN FORMS",skills)
       
        if not name:
            self.add_error('name', 'Name field cannot be empty.')

        if not age:
            self.add_error('age', 'Age field cannot be empty.')

        if not gender:
            self.add_error('age', 'Gender field cannot be empty.')

        if not skills:
            raise forms.ValidationError("Please select at least one skill.")
        
        return cleaned_data

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields =['name','age','adress','phone_number']