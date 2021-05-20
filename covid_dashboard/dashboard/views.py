from django.shortcuts import render

from . import maps, dataprocessing

# Create your views here.

def index(request):
    """The main dashboard"""
    data = dataprocessing.world_map_data()
    countries = dataprocessing.left_table(data[0])
    #print(countries)
    world_map = maps.world_map(data[0])
    context = {
        'countries': countries,
        'big_case_num': data[1],
        'world_map': world_map
    }
    return render(request, 'dashboard/index.html', context)