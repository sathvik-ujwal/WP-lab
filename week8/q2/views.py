from django.shortcuts import render, redirect
from .forms import UserForm

def first_page(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            request.session['name'] = form.cleaned_data['name']
            request.session['roll'] = form.cleaned_data['roll']
            request.session['subject'] = form.cleaned_data['subject']
            return redirect('second_page') 
    else:
        form = UserForm()
    return render(request, 'firstpage.html', {'form': form})

def second_page(request):
    name = request.session.get('name', '')
    roll = request.session.get('roll', '')
    subject = request.session.get('subject', '')
    return render(request, 'secondpage.html', {'name': name, 'roll': roll, 'subject': subject})
