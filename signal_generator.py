import numpy as np


def generate_sine(freq, fs, duration):
    """
    Function to generate sine wave

    Parameters:
    freq: Frequency of sine wave in Hz
    fs: sampling frequency in Hz
    duration: signal duration in seconds

    Returns:
    t: time array
    signal: generated sine wave values
    """

    t = np.arange(0, duration, 1/fs)
    signal = np.sin(2 * np.pi * freq * t)
    return t, signal
