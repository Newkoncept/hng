from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import get_latest_timestamp, get_latest_cat_fact

# Create your views here.
@api_view(["GET"])
def meview(request):
    data = {
        "status": "success",
        "user": {
            "email": "taiwoemmanuel15@gmail.com",
            "name": "Oluwagbemiga Taiwo",
            "stack": "Python/Django",

        },
        "timestamp": get_latest_timestamp(),
        "fact": get_latest_cat_fact()
    }
    return Response(data)