import matplotlib.pyplot as plt
import signal_generator
import output
import transform
import filters


# parameters
fs = 1000
freq = 5
duration = 1

# generate sine wave
t, signal = signal_generator.generate_sine(freq, fs, duration)
output.save_plot(t, signal, "Sine Wave", "Time",
                 "Amplitude", "sine_signal.png")


# add noise
noisy_signal = signal_generator.add_noise(signal, 0.5)
output.save_plot(t, noisy_signal, "Noisy sine wave",
                 "Time", "Amplitude", "noisy_signal.png")

# frequency spectrum
freq, spectrum, N = transform.compute_fft(signal, fs)
output.save_plot_fft(freq, spectrum, N,  "Frequency spectrum",
                     "Frequency", "Amplitude", "freq_spectrum.png")


# Low-pass
lpf = filters.apply_filter(noisy_signal, fs, "low", 10)
output.save_plot(t, lpf, "Low-pass Filtered", "Time", "Amplitude", "lpf.png")

# High-pass
hpf = filters.apply_filter(noisy_signal, fs, "high", 10)
output.save_plot(t, hpf, "High-pass Filtered", "Time", "Amplitude", "hpf.png")

# Band-pass
bpf = filters.apply_filter(noisy_signal, fs, "band", (3, 10))
output.save_plot(t, bpf, "Band-pass Filtered", "Time", "Amplitude", "bpf.png")

# Moving average
ma = filters.apply_filter(noisy_signal, fs, "moving_avg", 10)
output.save_plot(t, ma, "Moving Average", "Time", "Amplitude", "ma.png")
