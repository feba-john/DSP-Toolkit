import matplotlib.pyplot as plt
from signal_generator import generate_sine, add_noise

# parameters
fs = 1000
freq = 5
duration = 1

# function to generate sine wave
t, signal = generate_sine(freq, fs, duration)

# plots
plt.plot(t, signal)
plt.title("Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
# plt.savefig("results/output.png")
plt.show()

noisy_signal = add_noise(signal, 0.5)
plt.plot(t, noisy_signal)
plt.title("Noisy signal")
plt.savefig("results/output.png")
plt.show()
