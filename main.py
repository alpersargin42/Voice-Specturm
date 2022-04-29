import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile

Fs, aud = wavfile.read('c.wav')
aud = aud[:,0]
# ilk 125 saniyeyi kırp
first = aud[:int(Fs*125)]
powerSpectrum, frequenciesFound, time, imageAxis = plt.specgram(first, Fs=Fs)
plt.savefig('read.png')
plt.show()
