from django.db import models
from django.utils.timezone import now
from decimal import Decimal
import threading
from datetime import datetime, timedelta

class Authentication(models.Model):
    user_name = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user_name 

class Client(models.Model):
    user = models.ForeignKey(Authentication, on_delete=models.CASCADE, related_name="clients", null=True)

    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    start_date = models.DateField(default=now)

    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True,blank=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0 , null=True,blank=True)
    amount_add = models.DecimalField(max_digits=10, decimal_places=2, default=0 , null=True,blank=True)
    amount_delete = models.DecimalField(max_digits=10, decimal_places=2, default=0 , null=True,blank=True)

    interest = models.DecimalField(max_digits=10, decimal_places=2, default=0 , null=True,blank=True)
    interest_add = models.DecimalField(max_digits=10, decimal_places=2, default=0 , null=True,blank=True)
    interest_delete = models.DecimalField(max_digits=10, decimal_places=2, default=0 , null=True,blank=True)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0 , null=True,blank=True)

    STATUS_CHOICES = [
        ('process', 'Process'),
        ('complete', 'Complete')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='process')
 
    def __str__(self):
        return f"{self.name} - {self.contact_number}"
    
    @property
    def current_amount(self):
        amount_add = self.amount_add or Decimal('0.00')
        amount_delete = self.amount_delete or Decimal('0.00')
        return self.amount + amount_add - amount_delete

    @property
    def current_interest(self):
        interest_add = self.interest_add or Decimal('0.00')
        interest_delete = self.interest_delete or Decimal('0.00')
        return self.interest + interest_add - interest_delete

    def save(self, *args, **kwargs):
        # Update amount
        self.amount += self.amount_add or Decimal('0.00')
        self.amount -= self.amount_delete or Decimal('0.00')
        self.amount_add = Decimal('0.00')
        self.amount_delete = Decimal('0.00')

        # Update interest
        self.interest += self.interest_add or Decimal('0.00')
        self.interest -= self.interest_delete or Decimal('0.00')
        self.interest_add = Decimal('0.00')
        self.interest_delete = Decimal('0.00')

        # Update total amount
        self.total_amount = self.current_amount + self.interest

        # Save the updated model
        super().save(*args, **kwargs)

    def interest_growth(self):
        daily_interest = (self.current_amount * self.percentage ) / Decimal('100')
        return daily_interest
      
    def update_interest(self):
        self.interest += self.interest_growth()
        self.save()

    def update_total_amount(self):
        self.total_amount = self.current_amount + self.interest
        self.save()

    def __str__(self):
        return self.name
    
    @classmethod
    def update_interest_total_amount(cls):
        for client in cls.objects.filter(status='process'):
            client.update_interest()
            client.update_total_amount()

# Background thread to update all clients every 5 seconds
def update_clients_periodically():
    current_time = now()
    for client in Client.objects.filter(status='process'):
         # Check if 30 days have passed since the last start_date
         days_since_start = (current_time.date() - client.start_date).days
         if days_since_start >= 1:
             client.update_interest_total_amount()
             # Reset the start_date for the next cycle
             client.start_date = client.start_date + timedelta(days=30)
             client.save()

     # Schedule the next check (e.g., every 24 hours)
    threading.Timer(86400.0, update_clients_periodically).start()  # 86400 seconds = 24 hours


# Start the background thread when Django starts
# update_clients_periodically()