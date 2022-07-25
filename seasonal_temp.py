import xarray as xr
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs


path = '/nird/projects/NS9001K/sso102/CORDEX/data/tas/EUR-11/rcp85'
ncfile = xr.open_dataset(path + '/tas_mon_EUR-11_CLMcom_CCLM4-8-17_MPI-M-MPI-ESM-LR_r1i1p1_rcp85_1971-2099_SouthNorway.nc')
mean_data= ncfile.mean(dim='rlon').mean(dim='rlat').drop('lon_bnds').drop('lat_bnds').drop('rotated_latitude_longitude').drop('height')



time_year = pd.to_datetime(mean_data.time.values).strftime('%Y').unique()
y = np.zeros(len(time_year))
y[:] = np.nan

d = {"Jan": pd.Series(y, index=time_year),
     "Feb": pd.Series(y, index=time_year),
     "Mar": pd.Series(y, index=time_year),
     "Apr": pd.Series(y, index=time_year),
     "May": pd.Series(y, index=time_year),
     "Jun": pd.Series(y, index=time_year),
     "Jul": pd.Series(y, index=time_year),
     "Aug": pd.Series(y, index=time_year),
     "Sep": pd.Series(y, index=time_year),
     "Oct": pd.Series(y, index=time_year),
     "Nov": pd.Series(y, index=time_year),
     "Dec": pd.Series(y, index=time_year),
    }

df = pd.DataFrame(d)

aa=list(mean_data.groupby('time.month'))   
for m,(mm,mmm) in enumerate(aa): #loop through each month
  print('m')
  print(m)
  print('mm')
  print(mm)
  print('mmm')
  print(mmm)


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
