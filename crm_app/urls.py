from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, OrderViewSet,customer_list,order_list,campaign_list, create_campaign 

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('customers/', customer_list, name='customer_list'),
    path('orders/', order_list, name='order_list'),  # Add this line for the order_list URL pattern
    path('campaigns/', campaign_list, name='campaign_list'),
     path('campaigns/create/', create_campaign, name='create_campaign'),  # Add this line for the create_campaign URL pattern
]
