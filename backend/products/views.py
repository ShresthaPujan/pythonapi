from ast import Or
from rest_framework import generics,authentication,permissions

from .models import Product
from .serializers import ProductSerializer
from api.mixins import StaffEditorPermissionMixin ,UserQuerySetMixin
from api.permissions import IsStaffEditorPermission
class ProductListCreateAPIView(
    UserQuerySetMixin,
    IsStaffEditorPermission,generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

  

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        #email = serializer.validated_data.pop('email')
       # print(email)
        print(serializer.validated_data)
        title = serializer.validated_data.get( 'title')
        content = serializer.validated_data.get('content')  or None
        if content is None:
            content = title
        serializer.save(user=self.request.user,content=content)
    
    # def get_queryset(self , *args , **kwargs):
    #     qs = super().get_queryset(*args , **kwargs)
    #     request = self.request
    #     user = request.user
    #     if user.is_authenticated:
    #         return Product.objects.none( )
    #     print(request.user)
    #     return qs.filter(user=request.user )


product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

product_detail_view = ProductDetailAPIView.as_view()

class ProductListAPIView(StaffEditorPermissionMixin,generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   

product_list_view = ProductListAPIView.as_view()

class ProductUpdateAPIView(
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            ## 

product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()