import json
from django import views
# import requests

from django.views         import View
from django.http.response import JsonResponse



class GrammerView(View):
    def get(self, request):

        

        
        return JsonResponse({"MESSAGE": "Hello"}, status=200)


