import numpy as np
import time as t 

def get_sin_wave_amplitude(freq, time_point):
    return (np.sin(2 * np.pi * freq * time_point) + 1) / 2



def wait_for_sampling_period(sampling_frequency):
    t.sleep(1 / sampling_frequency)

def get_triangle_wave_amplitude(freq, time_point):
   
    period = 1.0 / freq
    phase = (time_point % period) / period  
    
    if phase < 0.5:
      
        return 2 * phase
    else:
      
        return 2 * (1 - phase)