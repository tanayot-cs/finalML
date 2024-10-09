import numpy as np
import joblib
import pandas as pd
from .forms import EnergyForm
from django.shortcuts import render
from datetime import datetime

# โหลดชุดข้อมูลการใช้พลังงาน
energy = pd.read_csv('dataset/cleaned_household_power_consumption.csv')

# โหลดโมเดล Gradient Boosting
gb = joblib.load('model/xgboost_model.pkl')

def energy_predict(request):
    result = None
    if request.method == 'POST':
        form = EnergyForm(request.POST)
        if form.is_valid():
            # รับค่าจากฟอร์ม
            Global_reactive_power = form.cleaned_data['Global_reactive_power']
            Voltage = form.cleaned_data['Voltage']
            Global_intensity = form.cleaned_data['Global_intensity']
            Sub_metering_1 = form.cleaned_data['Sub_metering_1']
            Sub_metering_2 = form.cleaned_data['Sub_metering_2']
            Sub_metering_3 = form.cleaned_data['Sub_metering_3']
            
            # เตรียมข้อมูลสำหรับการคาดการณ์
            input_data = np.array([[Global_reactive_power, Voltage, Global_intensity, Sub_metering_1, Sub_metering_2, Sub_metering_3]])
            
            # ทำการคาดการณ์
            prediction = gb.predict(input_data)[0]
            result = {
                'Global_active_power': prediction,
                'Global_reactive_power': Global_reactive_power,
                'Voltage': Voltage,
                'Global_intensity': Global_intensity,
                'Sub_metering_1': Sub_metering_1,
                'Sub_metering_2': Sub_metering_2,
                'Sub_metering_3': Sub_metering_3
            }
    else:
        form = EnergyForm()
    
    return render(request, 'energy_app/index.html', {'form': form, 'result': result})