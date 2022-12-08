#!/usr/bin/env python
# coding: utf-8

# # Visulizations for confusing concepts

# ## How can a wave's energy goes in opposite to its phase?

# It may be hard to picture how the shape of short Rossby waves propagate westwards (negative phase speed) while the energy of the waves propagate eastwrds (positive group speed). Well, in the below "moving picture", the upper panel shows a single short Rossby wave, the lower panel shows a superposition of two short Rossby waves. In which direction does a single wave/a wave group move?

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import holoviews as hv
import hvplot.xarray

def wave_generator(x_series, t_0, param_wave):
    y_ = np.zeros(len(x_series),)
    y_ = param_wave['A']*np.cos(param_wave['omega']*t_0-param_wave['k']*x_series)
    
    y = xr.DataArray(y_, dims=['x'],
                      coords={'x': x_series,
                              't': t_0})
    
    return y

# short rossby wave
param_wave = {
    'A' : 1, 
    'k' : 1,
}
param_wave['omega'] = -1/param_wave['k']
param_wave['c_ros'] = param_wave['omega']/param_wave['k']
param_wave1 = param_wave.copy()

param_wave = {
    'A' : 1, 
    'k' : 1.2,
}
param_wave['omega'] = -1/param_wave['k']
param_wave['c_ros'] = param_wave['omega']/param_wave['k']
param_wave2 = param_wave.copy()

x_series = np.arange(-100,0,.01)
t_0 = 1

hv.HoloMap({t_0: hv.Curve(wave_generator(x_series, t_0, param_wave2), label='f1(x)').opts(width=600) for t_0 in np.arange(0,40,1)}, 't')


# In[2]:


hv.HoloMap({t_0: hv.Curve(wave_generator(x_series, t_0, param_wave1)+wave_generator(x_series, t_0, param_wave2), label='f1(x)+f2(x)').opts(width=600) for t_0 in np.arange(0,40,1)}, 't')


# In[ ]:




