import mcp4725_driver as mcp4725
import signal_generator as sg
import time as t


amplitude = 3.3  # Амплитуда в Вольтах (максимум для MCP4725)
signal_frequency = 5  # Частота сигнала в Гц
sampling_frequency = 1000  # Частота дискретизации в Гц

if __name__ == "__main__":
    try:

        dac = mcp4725.MCP4725(3.3, 0x61, True)
        
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
      