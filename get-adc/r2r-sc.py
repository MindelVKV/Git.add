import time
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time

adc = None
try:
    dynamic_range = 3.3
    duration = 3.0
    
    adc = R2R_ADC(dynamic_range)
    
    voltage_values = []
    time_values = []
    
    start_time = time.time()
    
    while time.time() - start_time < duration:
        current_time = time.time() - start_time
        current_voltage = adc.get_sc_voltage()
        
        voltage_values.append(current_voltage)
        time_values.append(current_time)
        
        print(f"Время: {current_time:.1f} с, Напряжение: {current_voltage:.3f} В")
    
    plot_voltage_vs_time(time_values, voltage_values, dynamic_range)

finally:
    if adc is not None:
        adc.__del__()