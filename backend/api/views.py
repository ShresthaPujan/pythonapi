import json
from django.forms.models import model_to_dict
from django.http  import JsonResponse
from products.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request,*args, **kwargs):
    """
    DRF API VIEW
    """
    data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
        return Response(data)
   
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    # #    data = model_to_dict(model_data, fields=['id','title','price','sale_price'])
    #     data = ProductSerializer(instance).data
   