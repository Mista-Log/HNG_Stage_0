from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from datetime import datetime
import pytz





def get_current_datetime():
    tz = pytz.timezone('UTC')
    now = datetime.now(tz)
    return now.strftime('%Y-%m-%dT%H:%M:%SZ')

date = get_current_datetime()

class MyJsonView(View):
    def get(self, request, *args, **kwargs):
        data = {
        "email": "oloyedeibrahimsmile@gmail.com",
        "current_datetime": date,
        "github_url": "git@github.com:Mista-Log/HNG_Stage_0.git"
    }
        return JsonResponse(data)