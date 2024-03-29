import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('AGG')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import scipy.stats

# For Flask output
from io import BytesIO

class TimeSeriesPlotter(object):
    def __init__(self, datatable_path):
        self.df = pd.read_pickle(datatable_path)
        # Remove erroreneous data
        self.df = self.df[self.df.cloud>-5]

        self.df[['aod','cloud', 'vapor']] = self.df[['aod','cloud', 'vapor']].apply(scipy.stats.zscore)

        # Prepare an image for when someone clicks on data that isn't available
        with open("../assets/no_data.png", "rb") as f:
            self.error_img = BytesIO(f.read())

    def plot(self, lon, lat):
        lon = round(lon)
        lat = round(lat)
        onePoint = self.df[np.logical_and(self.df.long==lon, self.df.lat==lat)]

        if onePoint.size > 0:
            plt.figure(figsize=(6.4, 6.4), dpi=100)
            plt.plot(onePoint.day, onePoint.aod, label="Aerosols optical depth")
            plt.plot(onePoint.day, onePoint.cloud, label="Cloudiness")
            plt.plot(onePoint.day, onePoint.vapor, label="Atmospheric vapor")
            #plt.title(("Values at ({},{})".format(lon,lat)))
            plt.xlabel("Day in year 2017")
            plt.ylabel("Z-scored values")
            plt.legend()
            plt.tight_layout()
            png_output = BytesIO()
            canvas=FigureCanvas(plt.gcf())
            canvas.print_png(png_output)
            plt.clf()
        else:
            # No data
            png_output = self.error_img

        return png_output
