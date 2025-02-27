from django.shortcuts import render

def index(request):
    label_text = ""
    if request.method == "POST":
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        label_text = name + " " + message
        font_weight = 'normal'
        font_style = 'normal'
        text_decoration = 'none'
        text_color = 'black'

        if 'bold' in request.POST:
            font_weight = 'bold'
        if 'italic' in request.POST:
            font_style = 'italic'
        if 'underline' in request.POST:
            text_decoration = 'underline'
        
        if 'red' in request.POST:
            text_color = 'red'
        elif 'blue' in request.POST:
            text_color = 'blue'
        elif 'green' in request.POST:
            text_color = 'green'

        context = {
            'label_text': label_text,
            'font_weight': font_weight,
            'font_style': font_style,
            'text_decoration': text_decoration,
            'text_color': text_color
        }

        return render(request, 'index.html', context)

    return render(request, 'index.html', {})

