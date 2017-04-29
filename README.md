![banner](assets/banner.png)
KTH Team contributions for the NASA Space App Challenge 2017. Our team is working towards assiting in solving the problems described in the [Every Cloud Challenge](https://2017.spaceappschallenge.org/challenges/warning-danger-ahead/every-cloud/details).

Recent research indicates a relationship between the amount of aerosol particles in the atmosphere and different meterological conditions. This information could be used to predict the risk of severe storms before they happen. 

## Links
* [Mesoscale Convective Systems (MCS)](https://en.wikipedia.org/wiki/Mesoscale_convective_system)
* [Reading HDF files in Python](http://www.science-emergence.com/Articles/How-to-read-a-MODIS-HDF-file-using-python-/)
* [NASA MODIS Data](https://modis.gsfc.nasa.gov/data/)

## Instructions
* To run example script, in scripts folder:  
  `python read_data_example.py`
  this should print information about the content of the HDF file in assets/example_data/.
  
  ## Dependencies
* [HDF4](https://support.hdfgroup.org/)
* [Python-HDF4](https://pypi.python.org/pypi/python-hdf4)

  For plotting data in python
* [mpltoolkits.basemap](https://matplotlib.org/basemap/)

### Install instructions
STEP 1: Download HDF from https://support.hdfgroup.org/release4/cmakebuild.html
```
tar zxvf CMake-hdf-4.2.12.tar.gz
cd CMake-hdf-4.2.12
sudo apt-get install byacc flex
./configure --disable-fortran
make
make check
make install
```
STEP 2: Download Pyhdf from  https://pypi.python.org/pypi/python-hdf4
```
tar zxvf python-hdf4-0.9.tar.gz
cd python-hdf4-0.9
sudo python setup.py install
```
To plot in python: 
```
sudo apt-get install python-numpy python-matplotlib python-mpltoolkits.basemap
```



