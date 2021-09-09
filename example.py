import numpy as np
import pylab as pl
import iir_filter
from scipy import signal
#
data = np.loadtxt('ecg_50hz_1.dat')
data = data - 2048
data = data * 2E-3 * 500 / 1000
fs = 1000.0
#
pl.title('ECG')
#
y = data[:,1]
t = data[:,0]
pl.subplot(311)
pl.plot(t,y)
pl.xlabel('time/sec')
pl.ylabel('ECG/mV')
#
f0 = 48.0
f1 = 52.0
sos1 = signal.butter(4, [f0/fs*2,f1/fs*2], 'bandstop', output='sos')
f2 = 100
sos2 = signal.butter(4, f2/fs*2, output='sos')

iir1 = iir_filter.IIR_filter(sos1)
iir2 = iir_filter.IIR_filter(sos2)
y2 = np.zeros(len(y))
for i in range(len(y)):
    y2[i] = iir1.filter(iir2.filter(y[i]))

yf = np.fft.fft(y2) / len(y2)
yf[0] = 0

pl.subplot(312);
pl.plot(np.linspace(0,fs,len(yf)),20*np.log10(abs(yf)))
pl.xlabel('time/sec')
pl.ylabel('Spectrum/dB')
pl.xlim(0,fs/2)
#
#
pl.subplot(313)
pl.plot(t,y2)
pl.xlabel('time/sec')
pl.ylabel('ECG/mV')

pl.show()
