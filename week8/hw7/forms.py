from django import forms

class GroceryForm(forms.Form):
    grocery_items = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('wheat', 'Wheat - 40'),
            ('jaggery', 'Jaggery - 200'),
            ('dal', 'Dal - 80'),
        ],
        required=False,
        label="Select items"
    )
