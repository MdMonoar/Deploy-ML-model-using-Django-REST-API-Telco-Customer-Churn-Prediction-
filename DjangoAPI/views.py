from django.shortcuts import render

# Create your views here.

from .forms import CustomerForm
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
# from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Customer
from .serializer import CustomerSerializers

import pickle
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from sklearn.preprocessing import OrdinalEncoder

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers

def status(df):
    try:

        scaler = pickle.load(open("./DjangoAPI/Scaler.sav", 'rb'))
        model = pickle.load(open("./DjangoAPI/Model.sav", 'rb'))
        
        X = scaler.transform(df)
        y_pred = model.predict(X)
        y_pred = (y_pred>0.80)
        result = "Yes" if y_pred else "No"
        return result
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def FormView(request):
    if request.method == 'POST':
        form=CustomerForm(request.POST or None)

        if form.is_valid():
            customerID = form.cleaned_data['customerID']
            gender = form.cleaned_data['gender']
            SeniorCitizen = form.cleaned_data['SeniorCitizen']
            Partner = form.cleaned_data['Partner']
            Dependents = form.cleaned_data['Dependents']
            tenure = form.cleaned_data['tenure']
            PhoneService = form.cleaned_data['PhoneService']
            MultipleLines = form.cleaned_data['MultipleLines']
            InternetService = form.cleaned_data['InternetService']
            OnlineSecurity = form.cleaned_data['OnlineSecurity']
            OnlineBackup = form.cleaned_data['OnlineBackup']
            DeviceProtection = form.cleaned_data['DeviceProtection']
            TechSupport = form.cleaned_data['TechSupport']
            StreamingTV = form.cleaned_data['StreamingTV']
            StreamingMovies = form.cleaned_data['StreamingMovies']
            Contract = form.cleaned_data['Contract']
            PaperlessBilling = form.cleaned_data['PaperlessBilling']
            PaymentMethod = form.cleaned_data['PaymentMethod']
            MonthlyCharges = form.cleaned_data['MonthlyCharges']
            TotalCharges = form.cleaned_data['TotalCharges']

            df=pd.DataFrame({'customerID':[customerID], 'gender':[gender], 'SeniorCitizen':[SeniorCitizen],
             'Partner':[Partner], 'Dependents':[Dependents], 'tenure':[tenure],
             'PhoneService':[PhoneService], 'MultipleLines':[MultipleLines], 
             'InternetService':[InternetService], 'OnlineSecurity':[OnlineSecurity],
             'OnlineBackup':[OnlineBackup], 'DeviceProtection':[DeviceProtection],
             'TechSupport':[TechSupport], 'StreamingTV':[StreamingTV],
             'StreamingMovies':[StreamingMovies], 'Contract':[Contract],
             'PaperlessBilling':[PaperlessBilling], 'PaymentMethod':[PaymentMethod],
             'MonthlyCharges':[MonthlyCharges], 'TotalCharges':[TotalCharges]})
            
            ordenc = OrdinalEncoder()
            data = df.copy()
            encoded_data = pd.DataFrame()
            for i in data.columns :
                encoded_data[i] = data[i]
                if data[i].dtype == object:
                    encoded_col = np.array(data[i]).reshape(-1,1)
                    encoded_col = ordenc.fit_transform(encoded_col)
                    encoded_data[i] = encoded_col
            
            df = encoded_data

            result = status(df)
            return render(request, 'status.html', {"data": result})
        
    form=CustomerForm()
    return render(request, 'form.html', {'form': form})

