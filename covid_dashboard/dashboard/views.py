from django.shortcuts import render

# Create your views here.

def index(request):
    """The main dashboard"""
    countries = [
        ["USA",28212548,555,444],
        ["India",12000000,111,222],
        ["Brazil",5000000,63,22],
        ["USA",28212548,555,444],
        ["India",12000000,111,222],
        ["Brazil",5000000,63,22],
        ["USA",28212548,555,444],
        ["India",12000000,111,222],
        ["Brazil",5000000,63,22],
        ["USA",28212548,555,444],
        ["India",12000000,111,222],
        ["Brazil",5000000,63,22],
        ["USA",28212548,555,444],
        ["India",12000000,111,222],
        ["Brazil",5000000,63,22],
        ["USA",28212548,555,444],
        ["India",12000000,111,222],
        ["India",12000000,111,222],
        ["India",12000000,111,222],
        ["India",12000000,111,222],
        ["India",12000000,111,222],
        ["India",12000000,111,222],
        ["India",12000000,111,222],
        ["India",12000000,111,222],
        ["India",12000000,111,222],
        ["India",12000000,111,222],
        ["Bottom",5000000,63,22]
    ]
    context = {'countries': countries}
    return render(request, 'dashboard/index.html', context)