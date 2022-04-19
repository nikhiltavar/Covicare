from django.db import models

# Create your models here.

class Hospital (models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.DecimalField(max_digits=12, decimal_places=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    totalPatients = models.DecimalField(max_digits=5, decimal_places=0)
    totalBeds = models.DecimalField(max_digits=5, decimal_places=0)
    availableBeds = models.DecimalField(max_digits=5, decimal_places=0)
    totalVentillators = models.DecimalField(max_digits=5, decimal_places=0)
    availableVentillators = models.DecimalField(max_digits=5, decimal_places=0)
    totalInfusionPump = models.DecimalField(max_digits=5, decimal_places=0)
    availableInfusionPump = models.DecimalField(max_digits=5, decimal_places=0)
    totalO2Delivery = models.DecimalField(max_digits=5, decimal_places=0)
    availableO2Delivery = models.DecimalField(max_digits=5, decimal_places=0)
    O2cylinder = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self):
        return str(self.name)