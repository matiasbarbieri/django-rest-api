import json
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def api_home(request, *args, **kwatgs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id','title','price'])
    return Response(data)