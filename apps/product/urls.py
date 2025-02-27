from django.urls import path
from apps.product.views import ProductCreateAPIView, ProductListAPIView

urlpatterns = [
    path('product/', ProductListAPIView.as_view(), name="product"),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create')
]

