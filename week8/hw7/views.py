from django.shortcuts import render
from .forms import GroceryForm

def index(request):
    selected_items = []
    total_price = 0
    form = GroceryForm(request.POST or None)
    
    if form.is_valid():
        items = form.cleaned_data['grocery_items']
        prices = {
            'wheat': 40,
            'jaggery': 200,
            'dal': 80,
        }

        for item in items:
            selected_items.append((item, prices[item]))
            total_price += prices[item]
    
    return render(request, 'grocery.html', {'form': form, 'selected_items': selected_items, 'total_price': total_price})
