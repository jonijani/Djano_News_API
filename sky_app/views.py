from django.shortcuts import render
import json
from django.http import JsonResponse
from scrapping_code.scrapping import get_search_result 

def get_breaking_news(request,keyword):
    data = get_search_result(keyword)
    json_data = JsonResponse(data,safe=False)
    return json_data
    













