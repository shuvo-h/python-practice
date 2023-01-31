from django import forms

class UserForm(forms.Form):
    student_name = forms.CharField(label="Student's Name", max_length=100, required=True,widget=forms.TextInput(attrs={'class':"form-control"}))
    student_class = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':"form-control"}))
    student_DOB = forms.DateField(required=True)
