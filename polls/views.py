from django.shortcuts import render
from django.http import HttpResponse
from greytheory import GreyTheory
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

grey = GreyTheory()

@csrf_exempt
def index(request):
    if request.method == 'POST' :
        gm11 = grey.gm11

        patterns = [
            (223.3, ""),
            (227.3, ""),
            (230.5, ""),
            (238.1, ""),
            (242.9, ""),
            (251.1, "")
        ]

        for pattern in patterns:
            gm11.add_pattern(pattern[0], pattern[1])

        gm11.period = 2
        gm11.forecast()

        value_list = []
        for value in gm11.analyzed_results:
            value_list= value_list + [value.forecast_value]
        
        print(value_list[-1])
    return HttpResponse("Hello, world. You're at the polls index.")


