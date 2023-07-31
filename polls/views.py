import json
from django.shortcuts import render
from django.http import HttpResponse
from greytheory import GreyTheory
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

grey = GreyTheory()

@csrf_exempt
def index(request):
    if request.method == 'POST' :
        try:
            data = json.loads(request.body)
            timeDifferences = data.get('array', [])
        except Exception as e:
    # Handle the exception here
            print(f"An error occurred: {str(e)}")
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
            
            print(data)
            return HttpResponse(timeDifferences)


