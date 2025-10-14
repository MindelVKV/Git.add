import mcp4725_driver as mcp4725
import signal_generator as sg
import time as t

amplitude = 3.3  
signal_frequency = 10  
sampling_frequency = 1000  

if __name__ == "__main__":
    try:

        dac = mcp4725.MCP4725(3.3, 0x61, True)
        
        start_time = t.time()
        
        
        while True:
            
            current_time = t.time() - start_time
            
            i = sg.get_sin_wave_amplitude(signal_frequency, current_time)
            
            voltage = i * amplitude
            
            
            dac.set_voltage(voltage)
            
            sg.wait_for_sampling_period(sampling_frequency)
            

        
    finally:
     
        dac.deinit()
    