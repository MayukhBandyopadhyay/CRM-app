from django.shortcuts import render,redirect
from django.utils import timezone
from rest_framework import viewsets
from .models import Customer, Order,Campaign
from .serializers import CustomerSerializer, OrderSerializer
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def home(request):
    return render(request, 'home.html')  # Ensure you have a 'home.html' template in the templates folder
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})
def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'campaign_list.html', {'campaigns': campaigns})
def create_campaign(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        criteria = request.POST.get('criteria')
        if name and criteria:
            Campaign.objects.create(
                name=name,
                audience_criteria=criteria,
                created_at=timezone.now()
            )
            return redirect('campaign_list')
    return render(request, 'create_campaign.html')

