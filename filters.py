from scipy.signal import butter, filtfilt
import numpy as np


def apply_filter(signal, fs, filter_type, cutoff, order=4):
    """
    Function to analyse different types of filters

    Butterworth filter giving smooth response and no ripples
    order tells how sharp the filter transition is
    phase distortion cancelled using filtfilt()
    """
    nyquist = 0.5 * fs

    if filter_type == "low":
        norm_cutoff = cutoff / nyquist
        b, a = butter(order, norm_cutoff, btype='low')
        return filtfilt(b, a, signal)

    elif filter_type == "high":
        norm_cutoff = cutoff / nyquist
        b, a = butter(order, norm_cutoff, btype='high')
        return filtfilt(b, a, signal)

    elif filter_type == "band":
        low, high = cutoff
        b, a = butter(order, [low/nyquist, high/nyquist], btype='band')
        return filtfilt(b, a, signal)

    elif filter_type == "moving_avg":
        """
        moving average fiter: replace each point with the average of its neighboring values
        acting like LPF
        """
        window_size = int(cutoff)
        return np.convolve(signal, np.ones(window_size)/window_size, mode='same')

    else:
        raise ValueError("Invalid filter type")
