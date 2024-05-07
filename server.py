from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    f= open("Neighberhood_poverty.json", "r") 
    data = json.load(f)
    boroughs = list(data["borough"].keys())
    f.close()
    return render_template('index.html', boroughs=boroughs, data=data)

@app.route('/district')
def district():
    borough = request.args.get('borough')
  
    f= open("Neighberhood_poverty.json", "r") 
    data = json.load(f)
    Borough_districts = list(data["Districts"].keys())
    
    f.close()
    requestedData = {}

    for key in data:
        requestedData[key] = [round(data[key][Borough_districts][percent], 2)]
    colors = {}
    for i in range(1,11):
        colors[55.017 + i *(82.04878049 - 55.017)/10] = 100 - 10 * i

    
    for value in requestedData:
        for color in colors:
            if requestedData[value][0] < color:
                requestedData[value].append(colors[color])
                break

    return render_template('district.html', borough=borough, data=data, Borough_districts=Borough_districts, requestedData=requestedData)

@app.route('/borough')
def borough():
    f= open("Neighberhood_poverty.json", "r") 
    data = json.load(f)
    boroughs = list(data["borough"].keys())
    f.close()
    return render_template('borough.html', data=data, boroughs=boroughs)


app.run(debug=True)