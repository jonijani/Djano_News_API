from django.shortcuts import render
import json
from django.http import JsonResponse
from scrapping_code.scrapping import get_search_result ,BASE_URL

def get_breaking_news(request,keyword):
    #url = f"{BASE_URL}"
    data = get_search_result(keyword)
    #json_data = JsonResponse(data,safe=False)
    return JsonResponse(data, safe=False)













