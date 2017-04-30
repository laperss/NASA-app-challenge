from flask import Flask, request, jsonify, make_response
from tornadosCalculator import getTornadoCoords
from timeseriesPlotter import TimeSeriesPlotter


app = Flask(__name__, static_url_path='')

@app.route('/getTimeseries/<lon>/<lat>')
def getTimeseries(lon, lat):
    lon, lat = float(lon), float(lat)
    png_output = TSP.plot(lon,lat)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

@app.route('/getTornados/<lon>/<lat>')
def getTornados(lon, lat):
    lon, lat = float(lon), float(lat)
    response = {'tornadoCoords': getTornadoCoords(lon, lat)}
    return jsonify(response)

@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    TSP = TimeSeriesPlotter("../notebooks/datatable")
    app.run()
