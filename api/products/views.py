from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAdminUser, SAFE_METHODS, BasePermission, \
    DjangoModelPermissions


class ProductUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the vendor only.'

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.vendor == request.user


class ProductList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Product.postobjects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView, ProductUserWritePermission):
    permission_classes = [ProductUserWritePermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer