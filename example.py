import numpy as np
import pylab as pl
import scipy as sp
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
sos = signal.butter(2, [f0/fs*2,f1/fs*2], 'bandstop', output='sos')

f = iir_filter.IIR_filter(sos)
y2 = np.zeros(len(y))
for i in range(len(y)):
    y2[i] = f.filter(y[i])

yf = sp.fft(y2)
yf[0] = 0

pl.subplot(312);
pl.plot(sp.linspace(0,fs,len(yf)),abs(yf))
pl.xlabel('time/sec')
pl.ylabel('Spectrum')
pl.xlim(0,fs/2)
#
#
pl.subplot(313)
pl.plot(t,y2)
pl.xlabel('time/sec')
pl.ylabel('ECG/mV')

pl.show()
