import matplotlib.pyplot as plt
import signal_generator
import output
import transform

# parameters
fs = 1000
freq = 5
duration = 1

# function to generate sine wave
t, signal = signal_generator.generate_sine(freq, fs, duration)
output.save_plot(t, signal, "Sine Wave", "Time",
                 "Amplitude", "sine_signal.png")


# function to add noise
noisy_signal = signal_generator.add_noise(signal, 0.5)
output.save_plot(t, noisy_signal, "Noisy sine wave",
                 "Time", "Amplitude", "noisy_signal.png")

# function for transform signal
freq, spectrum = transform.compute_fft(signal, fs)
output.save_plot(freq, spectrum, "Frequency spectrum",
                 "Frequency", "Amplitude", "freq_spectrum.png")
