=======================================
Efficient realtime IIR filter in Python
=======================================

This is an IIR filter class which performs sample by sample realtime
processing of data. It's very efficient because it's not using any 
indexing operations internally. The class instance acts as the memory
of the filter so that it remembers its past.

Installation
============

Install form the python package index with::

  pip install py-iir-filter

You can also install it locally from the cloned github repo with::

  python setup.py install


Import
======

Use the standard python command to import it::

  import iir_filter


Calculate the coefficients
==========================

Use your favourite scipy IIR design command and export the coefficients as an SOS::

    sos = signal.butter(order, [cutoff(s)], '[filter type]', output='sos')



Create an instance
==================

The constructor takes the sos chain as an argument::

    f = iir_filter.IIR_filter(sos)



Perform filtering sample by sample
==================================

Filtering is sample by sample by processing the samples
as they arrive, for example from an ADC::

   sample = f.filter(sample)
