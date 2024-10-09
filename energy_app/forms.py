from django import forms

class EnergyForm(forms.Form):
    Global_reactive_power = forms.FloatField(label='Global Reactive Power')
    Voltage = forms.FloatField(label='Voltage')
    Global_intensity = forms.FloatField(label='Global Intensity')
    Sub_metering_1 = forms.FloatField(label='Sub Metering 1')
    Sub_metering_2 = forms.FloatField(label='Sub Metering 2')
    Sub_metering_3 = forms.FloatField(label='Sub Metering 3')
