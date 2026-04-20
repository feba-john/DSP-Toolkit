import numpy as np


def compute_fft(signal, fs):
    """
    Function to find the frequency of signal

    Peak at frequency but weak strength for other frequency
    """
    fft_val = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), 1/fs)
    return freqs, abs(fft_val), len(signal)
