from flask import Flask 
from flask import render_template, redirect, request

from geopy.geocoders import Nominatim
import time 

app = Flask(__name__)

pop = Nominatim(user_agent="google")
def location_by_address(address):
    time.sleep(1)
    try:
        return pop.geocode(address).raw
    except:
        return location_by_address(address)



def address_by_location(latitude, longitude):
    cordinates = f"{latitude},{longitude}"
    time.sleep(1)
    try:
        return pop.reverse(cordinates, language="en")
    except:
        return address_by_location(latitude, longitude)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/street',methods=['POST','GET'])
def street():
    if request.method == "POST":
        street = request.form.get('street')
        location = location_by_address(street)
        context = {
            'latitude':location['lat'],
            'longitude':location['lon']
        }
        return render_template('street.html',latitude=location['lat'], longitude=location['lon'])
    return render_template('street.html')

@app.route('/coord', methods=['POST','GET'])
def coord():
    if request.method == "POST":
        lat = request.form.get('lat')
        long = request.form.get('long')
        #address = address_by_location(lat,long)
        return render_template('coord.html',address = address_by_location(lat,long))
    return render_template('coord.html')


if __name__ == "__main__":
    app.run(debug=True)