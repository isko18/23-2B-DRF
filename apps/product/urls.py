from django.urls import path
from apps.product.views import ProductCreateAPIView

urlpatterns = [
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create')
]

