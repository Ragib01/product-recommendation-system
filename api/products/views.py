from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import ProductListSerializer, ProductSerializer, ProductTypeSerializer, WeatherTypeSerializer
from rest_framework.permissions import IsAdminUser, SAFE_METHODS, BasePermission, \
    DjangoModelPermissions


class IsVendorUserPermission(BasePermission):
    message = 'Creating products is restricted to the vendor only.'

    def has_permission(self, request, view):
        # allow user to list all users if logged in user is staff
        return request.user.is_vendor


class ProductUserWritePermission(BasePermission):
    message = 'Editing products is restricted to the vendor only.'

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.vendor == request.user


class ProductTypeList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]  # only for admin users
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]  # only for admin users
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class WeatherTypeList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]  # only for admin users
    queryset = WeatherType.objects.all()
    serializer_class = WeatherTypeSerializer


class WeatherTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]  # only for admin users
    queryset = WeatherType.objects.all()
    serializer_class = WeatherTypeSerializer


class ProductList(generics.ListCreateAPIView):
    permission_classes = [IsVendorUserPermission]
    queryset = Product.postobjects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView, ProductUserWritePermission):
    permission_classes = [ProductUserWritePermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductView(APIView):

    # search by item name or weather type
    def get(self, request):
        name = self.request.query_params.get('item_name')
        weather = self.request.query_params.get('weather_type')

        if name or weather:
            queryset = Product.objects.filter(item_name=name) | Product.objects.filter(weather_type__name=weather)
        else:
            queryset = Product.objects.all()
        serializer = ProductListSerializer(queryset, many=True)
        return Response({'count': len(serializer.data), 'data': serializer.data})
