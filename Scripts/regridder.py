import pandas as pd
import numpy as np
import xarray as xr
import xesmf as xe

ds_cci = xr.open_dataset('../Data/hycom_cci_sst.nc')
ds_cci = ds_cci.sel(time=slice('2009-01-01','2014-06-04'))

ds_sst = xr.open_dataset('../Data/cci_sst.nc')
ds_sst = ds_sst.sel(time=slice('2009-01-01','2014-06-04'))
ds_sst['analysed_sst'] = ds_sst['analysed_sst'] - 273.15

ds_cci = ds_cci.rename({'latitude': 'lat', 'longitude': 'lon'})

regridder = xe.Regridder(ds_sst, ds_cci, 'bilinear')
regridder.clean_weight_file()

ds_sst_regridded = regridder(ds_sst)
ds_sst_regridded.to_netcdf('../Data/cci_sst_xesmf.nc')
