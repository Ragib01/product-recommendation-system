from django.urls import path
from .views import ProductView, ProductDetail, ProductList, ProductTypeList, ProductTypeDetail, WeatherTypeDetail, \
    WeatherTypeList

app_name = 'products'

urlpatterns = [
    path('<int:pk>/', ProductDetail.as_view(), name='detailcreate'),
    path('', ProductList.as_view(), name='listcreate'),
    path('search/', ProductView.as_view() ),
    path('product-type/<int:pk>/', ProductTypeDetail.as_view(), name='typedetailcreate'),
    path('product-type/', ProductTypeList.as_view(), name='typelistcreate'),
    path('weather-type/<int:pk>/', WeatherTypeDetail.as_view(), name='weatherdetailcreate'),
    path('weather-type/', WeatherTypeList.as_view(), name='weatherlistcreate'),
]