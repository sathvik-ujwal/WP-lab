from django import forms

class CarForm(forms.Form):
    MANUFACTURERS = [
        ('toyota', 'Toyota'),
        ('ford', 'Ford'),
        ('honda', 'Honda'),
        ('bmw', 'BMW'),
        ('audi', 'Audi'),
    ]
    
    manufacturer = forms.ChoiceField(choices=MANUFACTURERS, label="Car Manufacturer")
    model = forms.CharField(max_length=100, label="Car Model")
