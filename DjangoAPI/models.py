from django.db import models

# Create your models here.

class Customer(models.Model ):
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'))
    BINARY_CHOICES = (('Yes', 'Yes'), ('No', 'No'))
    LINE_CHOICES = (('Yes', 'Yes'), ('No', 'No'), ('No phone service', 'No phone service'))
    INTERNET_CHOICES = (('DSL', 'DSL'), ('Fiber optic', 'Fiber optic'), ('No', 'No'))
    NET_SERVICE_CHOICES = (('Yes', 'Yes'),('No', 'No'),('No internet service', 'No internet service'))
    CONTRACT_CHOICES = (('Month-to-month', 'Month-to-month'), ('One year', 'One year'), ('Two year', 'Two year'))
    PAYMENT_CHOICES = (('Electronic check', 'Electronic check'), ('Mailed check', 'Mailed check'), ('Bank transfer (automatic)', 'Bank transfer (automatic)'), ('Credit card (automatic)', 'Credit card (automatic)'))

    customerID = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    SeniorCitizen = models.CharField(max_length=6, choices=BINARY_CHOICES)
    Partner = models.CharField(max_length=6, choices=BINARY_CHOICES)
    Dependents = models.CharField(max_length=6, choices=BINARY_CHOICES)
    tenure = models.IntegerField()
    PhoneService = models.CharField(max_length=6, choices=BINARY_CHOICES)
    MultipleLines = models.CharField(max_length=20, choices=LINE_CHOICES)
    InternetService = models.CharField(max_length=20, choices=INTERNET_CHOICES)
    OnlineSecurity = models.CharField(max_length=20, choices=NET_SERVICE_CHOICES)
    OnlineBackup = models.CharField(max_length=20, choices=NET_SERVICE_CHOICES)
    DeviceProtection = models.CharField(max_length=20, choices=NET_SERVICE_CHOICES)
    TechSupport = models.CharField(max_length=20, choices=NET_SERVICE_CHOICES)
    StreamingTV = models.CharField(max_length=20, choices=NET_SERVICE_CHOICES)
    StreamingMovies = models.CharField(max_length=20, choices=NET_SERVICE_CHOICES)
    Contract = models.CharField(max_length=20, choices=CONTRACT_CHOICES)
    PaperlessBilling = models.CharField(max_length=6, choices=BINARY_CHOICES)
    PaymentMethod = models.CharField(max_length=30, choices=PAYMENT_CHOICES)
    MonthlyCharges = models.FloatField()
    TotalCharges = models.FloatField()

    def __str__(self):
        return self.gender

