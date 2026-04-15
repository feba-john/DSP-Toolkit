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


def add_noise(signal, noise_level):
    """
    add Gaussian (white) noise to sine signal generated

    Args:
        signal : Input signal array
        noise_level (float): Scaling factor controlling noise amplitude

    Returns:
        Noisy signal obtained by adding Gaussian noise
    """

    noise = noise_level * np.random.randn(len(signal))
    return signal + noise
