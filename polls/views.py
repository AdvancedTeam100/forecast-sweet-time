from django.shortcuts import render
from django.http import HttpResponse
from greytheory import GreyTheory

# Create your views here.

grey = GreyTheory()

def index(request):
    gm11 = grey.gm11

    gm11.add_pattern(223.3, "a1")
    gm11.add_pattern(227.3, "a2")
    gm11.add_pattern(230.5, "a3")
    gm11.add_pattern(238.1, "a4")
    gm11.add_pattern(242.9, "a5")
    gm11.add_pattern(251.1, "a6")

    gm11.period = 2 # Default is 1, the parameter means how many next moments need to forcast continually.
    gm11.forecast()
    #forecasted_results = gm11.forecasted_outputs()
    #gm11.print_forecasted_results()

    value_list = []
    for value in gm11.analyzed_results:
        value_list.append(value.forecast_value)
    
    print(value_list[-1])
    return HttpResponse("Hello, world. You're at the polls index.")

