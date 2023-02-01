# Generated by Django 4.1.5 on 2023-01-31 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('SeniorCitizen', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=6)),
                ('Partner', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=6)),
                ('Dependents', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=6)),
                ('tenure', models.IntegerField()),
                ('PhoneService', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=6)),
                ('MultipleLines', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('No phone service', 'No phone service')], max_length=20)),
                ('InternetService', models.CharField(choices=[('DSL', 'DSL'), ('Fiber optic', 'Fiber optic'), ('No', 'No')], max_length=20)),
                ('OnlineSecurity', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('No internet service', 'No internet service')], max_length=20)),
                ('OnlineBackup', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('No internet service', 'No internet service')], max_length=20)),
                ('DeviceProtection', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('No internet service', 'No internet service')], max_length=20)),
                ('TechSupport', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('No internet service', 'No internet service')], max_length=20)),
                ('StreamingTV', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('No internet service', 'No internet service')], max_length=20)),
                ('StreamingMovies', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('No internet service', 'No internet service')], max_length=20)),
                ('Contract', models.CharField(choices=[('Month-to-month', 'Month-to-month'), ('One year', 'One year'), ('Two year', 'Two year')], max_length=20)),
                ('PaperlessBilling', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=6)),
                ('PaymentMethod', models.CharField(choices=[('Electronic check', 'Electronic check'), ('Mailed check', 'Mailed check'), ('Bank transfer (automatic)', 'Bank transfer (automatic)'), ('Credit card (automatic)', 'Credit card (automatic)')], max_length=30)),
                ('MonthlyCharges', models.IntegerField()),
                ('TotalCharges', models.IntegerField()),
            ],
        ),
    ]
