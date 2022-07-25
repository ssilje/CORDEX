import xarray as xr

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs

# Read the data
path = '/nird/projects/NS9001K/sso102/CORDEX/data/tas/EUR-11/rcp85'
# cropped out southern norway from a cordex file.
ncfile = xr.open_dataset(path + '/tas_mon_EUR-11_CLMcom_CCLM4-8-17_MPI-M-MPI-ESM-LR_r1i1p1_rcp85_1971-2099_SouthNorway.nc')

# calculate area mean

mean_data= ncfile.mean(dim='rlon').mean(dim='rlat').drop('lon_bnds').drop('lat_bnds').drop('rotated_latitude_longitude').drop('height')

# Make a dataframe with month vs year

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

# Sorth the data by month and place them in the dataframe
aa=list(mean_data.groupby('time.month'))   
for m,(mm,mmm) in enumerate(aa): #loop through each month
  df.iloc[:,m]= mmm.tas.values  


## Plotting 

plt.clf()
plt.contourf(np.linspace(1, 12,12), np.linspace(1971, 2099, 129), df.values, cmap='magma_r');
plt.xticks(np.linspace(1, 12,12),df.columns, rotation='vertical')
plt.ylabel('Year')  
plt.colorbar();
plt.savefig('tas_month_vs_year.png')
