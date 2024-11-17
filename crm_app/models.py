from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    total_spending = models.FloatField()
    visits = models.IntegerField()
    last_visit_date = models.DateField()

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_amount = models.FloatField()
    order_date = models.DateField()

    def __str__(self):
        return f'Order {self.id} by {self.customer.name}'

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    audience_criteria = models.TextField()  # Stores criteria in JSON or text format

    def __str__(self):
        return self.name

class CommunicationLog(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('SENT', 'Sent'), ('FAILED', 'Failed')])
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Log for {self.campaign.name} to {self.customer.name}'

