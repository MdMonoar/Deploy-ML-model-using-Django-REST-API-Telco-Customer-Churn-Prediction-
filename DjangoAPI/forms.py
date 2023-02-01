from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

        GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
        BINARY_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
        LINE_CHOICES = [('Yes', 'Yes'), ('No', 'No'), ('No phone service', 'No phone service')]
        INTERNET_CHOICES = [('DSL', 'DSL'), ('Fiber optic', 'Fiber optic'), ('No', 'No')]
        NET_SERVICE_CHOICES = [('Yes', 'Yes'),('No', 'No'),('No internet service', 'No internet service')]
        CONTRACT_CHOICES = [('Month-to-month', 'Month-to-month'), ('One year', 'One year'), ('Two year', 'Two year')]
        PAYMENT_CHOICES = [('Electronic check', 'Electronic check'), ('Mailed check', 'Mailed check'), ('Bank transfer (automatic)', 'Bank transfer (automatic)'), ('Credit card (automatic)', 'Credit card (automatic)')]

        gender = forms.TypedChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
        SeniorCitizen = forms.TypedChoiceField(choices=BINARY_CHOICES)
        Partner = forms.TypedChoiceField(choices=BINARY_CHOICES)
        Dependents = forms.TypedChoiceField(choices=BINARY_CHOICES)
        tenure = forms.IntegerField()
        PhoneService = forms.TypedChoiceField(choices=BINARY_CHOICES)
        MultipleLines = forms.TypedChoiceField(choices=LINE_CHOICES)
        InternetService = forms.TypedChoiceField(choices=INTERNET_CHOICES)
        OnlineSecurity = forms.TypedChoiceField(choices=NET_SERVICE_CHOICES)
        OnlineBackup = forms.TypedChoiceField(choices=NET_SERVICE_CHOICES)
        DeviceProtection = forms.TypedChoiceField(choices=NET_SERVICE_CHOICES)
        TechSupport = forms.TypedChoiceField(choices=NET_SERVICE_CHOICES)
        StreamingTV = forms.TypedChoiceField(choices=NET_SERVICE_CHOICES)
        StreamingMovies = forms.TypedChoiceField(choices=NET_SERVICE_CHOICES)
        Contract = forms.TypedChoiceField(choices=CONTRACT_CHOICES)
        PaperlessBilling = forms.TypedChoiceField(choices=BINARY_CHOICES)
        PaymentMethod = forms.TypedChoiceField(choices=PAYMENT_CHOICES)
        MonthlyCharges = forms.FloatField()
        TotalCharges = forms.FloatField()