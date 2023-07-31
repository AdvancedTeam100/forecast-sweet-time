from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from greytheory import GreyTheory

# Create your views here.

grey = GreyTheory()

def index(request):
    if request.method == 'POST':
        data = request.POST.getlist('array')
        gm11 = grey.gm11

        for value in data:
            gm11.add_pattern(float(value), "")

        gm11.period = 2
        gm11.forecast()

        value_list = []
        for value in gm11.analyzed_results:
            value_list.append(value.forecast_value)

        result = {
            'forecast_value': value_list[-1]
        }

        return JsonResponse(result)
    else:
        return HttpResponse("Invalid request method.")


