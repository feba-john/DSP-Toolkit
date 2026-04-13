import matplotlib.pyplot as plt 
from signal_generator import generate_sine

#parameters
fs = 1000
freq = 5
duration  = 1

#function to generate sine wave
t, signal = generate_sine(freq, fs, duration)

#plots
plt.plot(t, signal)
plt.title("Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()

