import numpy as np
import matplotlib.pyplot as plt

def voiced_excitation(duration, F0, Fs):
   
    excitation = np.zeros(duration)
    period = int(np.round(Fs / F0))
    excitation[::period] = -1
    return excitation

def resonator(x, F, BW, Fs):
    
    N = len(x)
    y = np.zeros(N)
    
    r = np.exp(-np.pi * BW / Fs)
    theta = 2 * np.pi * F / Fs
    a1 = -2 * r * np.cos(theta)
    a2 = r**2

    for n in range(2, N):
        y[n] = x[n] + a1 * y[n-1] + a2 * y[n-2]
    
    return y

def synthesize_vowel(duration, F0, F1, F2, F3, F4, BW1, BW2, BW3, BW4, Fs):
   
    excitation = voiced_excitation(duration, F0, Fs)
    
    y1 = resonator(excitation, F1, BW1, Fs)
    y2 = resonator(y1, F2, BW2, Fs)
    y3 = resonator(y2, F3, BW3, Fs)
    y4 = resonator(y3, F4, BW4, Fs)
    
    return y4


import importlib, grade
importlib.reload(grade)


excitation = voiced_excitation(8000, 110, 8000)
fig=plt.figure(figsize=(14,4),tight_layout=True)
subfig=fig.subplots(1,1)
subfig.stem(excitation[:300])  
subfig.set_title('The first 300 samples of a simple speech excitation signal',fontsize=24)
plt.show()


Fs = 8000
resonance = resonator(excitation, 500, 100, Fs)
fig=plt.figure(figsize=(14,4),tight_layout=True)
subfig=fig.subplots(1,1)
subfig.plot(resonance[:300])  
subfig.set_title('Excitation passed through a 500Hz resonator',fontsize=24)
plt.show()


fig = plt.figure(figsize=(14,15),tight_layout=True)
subfig = fig.subplots(5,1)

F0 = 110
F1 = {'a': 730, 'i': 270, 'u': 300, 'e': 530, 'o': 570}
F2 = {'a': 1090, 'i': 2290, 'u': 870, 'e': 1840, 'o': 840}

for plotnum, phoneme in enumerate('aiueo'):
    speech = synthesize_vowel(8000, F0, F1[phoneme], F2[phoneme], 2500, 3500, 100, 200, 300, 400, Fs)
    
    subfig[plotnum].plot(speech[:300])
    subfig[plotnum].set_title('Artificial /%s/'%(phoneme),fontsize=24)

plt.show()
