from playsound import playsound

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
from scipy.io import wavfile

samplerate, data = wavfile.read("sino.wav")
print(samplerate)
print(data.shape)
print(data.size)
samples = data.shape[0]
print(samples)
plt.plot(data[:3*samplerate])
plt.show();
from scipy.fftpack import fft,fftfreq

datafft = fft(data)
#Get the absolute value of real and complex component:
fftabs = abs(datafft)

freqs = fftfreq(samples,1/samplerate)

plt1.plot(freqs,fftabs)
plt1.show();

plt2.xlim( [10, samplerate/2] )
plt2.xscale( 'log' )
plt2.grid( True )
plt2.xlabel( 'Frequency (Hz)' )
plt2.plot(freqs[:int(freqs.size/2)],fftabs[:int(freqs.size/2)])


	playsound('sino.mp3')
