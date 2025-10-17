import os
from rest_framework.decorators import api_view
from django.views.decorators.cache import never_cache
from rest_framework.response import Response
from .utils import get_latest_timestamp, get_latest_cat_fact

# Create your views here.
@api_view(["GET"])
@never_cache
def meview(request):
    data = {
        "status": "success",
        "user": {
            "email": os.getenv("PROFILE_EMAIL"),
            "name": os.getenv("PROFILE_NAME"),
            "stack": os.getenv("PROFILE_STACK"),

        },
        "timestamp": get_latest_timestamp(),
        "fact": get_latest_cat_fact()
    }
    return Response(data)