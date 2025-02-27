from django import forms

class UserForm(forms.Form):
    SUBJECT_CHOICES = [
        ('Mathematics', 'Mathematics'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
        ('Biology', 'Biology'),
        ('Computer Science', 'Computer Science'),
    ]
    
    name = forms.CharField(max_length=100, label='Name')
    roll = forms.CharField(max_length=10, label='Roll Number')
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, label='Subject')
