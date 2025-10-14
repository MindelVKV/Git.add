import r2r_dac as r2r
import signal_generator as sg
import time as t


amplitude = 3.2  # Амплитуда в Вольтах
signal_frequency = 5  # Частота сигнала в Гц
sampling_frequency = 1000  # Частота дискретизации в Гц

if __name__ == "__main__":
    try:
        
        dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, True)
        
        start_time = t.time()
    
        
        while True:
   
            current_time = t.time() - start_time

            triangle_amplitude = sg.get_triangle_wave_amplitude(signal_frequency, current_time)
            

            voltage = triangle_amplitude * amplitude
            

            dac.set_voltage(voltage)
            
            
            sg.wait_for_sampling_period(sampling_frequency)
            
    except KeyboardInterrupt:
        print("\nГенерация сигнала остановлена пользователем")
        
    finally:
        
        dac.deinit()
      