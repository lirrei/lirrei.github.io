import numpy as np


def waveform_to_frames(waveform, frame_length, step):
    N = len(waveform)
    num_frames = int((N - frame_length) / step) + 1
    frames = np.zeros((frame_length, num_frames))

    for t in range(num_frames):
        start = t * step
        frames[:, t] = waveform[start:start + frame_length]

    return frames


import numpy as np


def frames_to_stft(frames):
    frame_length, num_frames = frames.shape
    stft = np.zeros_like(frames, dtype=np.complex128)

    for t in range(num_frames):
        stft[:, t] = np.fft.fft(frames[:, t])

    return stft


import numpy as np


def stft_to_spectrogram(stft):
    abs_stft = np.abs(stft)
    spectrogram = 20 * np.log10(abs_stft + np.finfo(float).eps)

    max_val = np.max(spectrogram)
    min_val = np.max(spectrogram) - 60.0  # Ensure minimum value is no smaller than -60dB

    spectrogram = np.maximum(spectrogram, min_val)

    return spectrogram
