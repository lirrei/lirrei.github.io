import numpy as np


def dft_matrix(N):

    W = np.zeros((N, N), dtype='complex')
    for k in range(N):
        for n in range(N):
            W[k, n] = np.cos(2 * np.pi * k * n / N) - 1j * np.sin(2 * np.pi * k * n / N)
    return W
