
import xarray as xr
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs


path = '/nird/projects/NS9001K/sso102/CORDEX/data/tas/EUR-11/rcp85'
ncfile = xr.open_dataset(path + '/tas_day_EUR-11_CLMcom_CCLM4-8-17_MPI-M-MPI-ESM-LR_r1i1p1_rcp85_1971-2099.nc')



## Plotting 

varplot = ncfile.tas.sel(time='1971-01-01')
#levels_plot = np.linspace(round(np.nanmin(dataopen_ymonmean.swvl1)),round(np.nanmax(dataopen_ymonmean.swvl1)),21)
#levels_cbar = np.linspace(round(np.nanmin(dataopen_ymonmean.swvl1)),round(np.nanmax(dataopen_ymonmean.swvl1)),11)
levels_plot = np.linspace(240,300,21)
levels_cbar = np.linspace(240,300,11)
plot_title  = 'test (1971) ' + varplot.long_name
fname       = 'tas'
label_text  = varplot.units

im = varplot.plot(
  x               = 'lon',
  y               = 'lat',
  col              = 'time',
  col_wrap         = 3,
  levels           = levels_plot,
  subplot_kws      = dict(projection=ccrs.PlateCarree()),
  transform        = ccrs.PlateCarree(),
  cbar_kwargs      = {'label': label_text, 'ticks': levels_cbar}
        )

  
for i,ax in enumerate(im.axes.flat):
  ax.coastlines(resolution = '10m', 
                color      = 'black',
                linewidth  = 0.2)
  ax.set_title(dataopen_ymonmean.time[i].dt.month.values)
        
plt.suptitle(plot_title)

plt.savefig(fname+'.png',dpi='figure',bbox_inches='tight')
plt.close()
print('Figure stored at: '+fname+'.png')
