from flask import Flask, request, jsonify
from tornadosCalculator import getTornadoCoords

app = Flask(__name__, static_url_path='')

@app.route('/getTornados/<lon>/<lat>')
def getTornados(lon, lat):
    lon, lat = float(lon), float(lat)
    response = {'tornadoCoords': getTornadoCoords(lon, lat)}
    return jsonify(response)

@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run()
