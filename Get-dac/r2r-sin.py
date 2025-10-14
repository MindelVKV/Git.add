import r2r_dac as r2r
import signal_generator as sg
import time as t

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        start_time = t.time()
        dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, True)
        while True:
            correct_time = t.time() - start_time
            i = sg.get_sin_wave_amplitude(signal_frequency, correct_time)
            sv = i * amplitude
            dac.set_voltage(sv)  
            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        dac.deinit()