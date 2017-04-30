import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('AGG')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt

# For Flask output
from io import BytesIO

class TimeSeriesPlotter(object):
    def __init__(self, datatable_path):
        self.df = pd.read_pickle(datatable_path)
        # Remove erroreneous data
        self.df = self.df[self.df.cloud>-5]

        # Prepare an image for when someone clicks on data that isn't available
        with open("../assets/no_data.png", "rb") as f:
            self.error_img = BytesIO(f.read())

    def plot(self, lon, lat):
        lon = round(lon)
        lat = round(lat)
        onePoint = self.df[np.logical_and(self.df.long==lon, self.df.lat==lat)]
        #fig = Figure()
        #plt.figure(fig)

        if onePoint.size > 0:
            plt.plot(onePoint.day, onePoint.aod, label="Aerosols")
            plt.plot(onePoint.day, onePoint.cloud, label="Cloudiness")
            plt.plot(onePoint.day, onePoint.vapor, label="Atmospheric vapor")
            plt.title(("Values at ({},{})".format(lon,lat)))
            plt.xlabel("Day in year 2017")
            plt.ylabel("Arbitrary and different units")
            plt.legend()
            png_output = BytesIO()
            canvas=FigureCanvas(plt.gcf())
            canvas.print_png(png_output)
            plt.clf()
        else:
            # No data
            png_output = self.error_img

        #plt.show()
        return png_output
