import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from greytheory import GreyTheory
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

grey = GreyTheory()

@csrf_exempt
def index(request):
    if request.method == 'POST':
        # data = request.body.decode('utf-8')
        print(request)
        array = []
        # try:
        #     json_data = json.loads(data)
        #     array = json_data.get('array', [])
        # except json.JSONDecodeError as e:
        #     print("Error decoding JSON:", str(e))
                
        # gm11 = grey.gm11

        # for value in array:
        #     gm11.add_pattern(float(value), "")

        # gm11.period = 2
        # gm11.forecast()

        # value_list = []
        # for value in gm11.analyzed_results:
        #     value_list.append(value.forecast_value)

        # result = {
        #     'forecast_value': value_list[-1]
        # }

        return JsonResponse("result")
    else:
        return HttpResponse("Invalid request method.")


