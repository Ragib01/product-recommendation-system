from django.urls import path
from .views import ProductList, ProductDetail, ProductView

app_name = 'products'

urlpatterns = [
    # path('<int:pk>/', ProductDetail.as_view(), name='detailcreate'),
    # path('', ProductList.as_view(), name='listcreate'),
    path('', ProductView.as_view() ),
]