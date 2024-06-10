from flask import Flask
from flask import render_template
from flask import request
import json
import logging


app = Flask(__name__, static_url_path='', static_folder='static')

"logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w',format='%(name)s - %(levelname)s - %(message)s')"
@app.route('/')
def index():
    f= open("Neighberhood_poverty.json", "r") 
    data = json.load(f)
    boroughs = list(data["borough"].keys())
    f.close()
    f= open("Neighberhood_poverty.json", "r") 
    data = json.load(f)
    Borough_districts = list(data["Districts"])
    print("borough", Borough_districts)
    return render_template('index.html', boroughs=boroughs, data=data, Borough_districts=Borough_districts)

@app.route('/district/<borough_type>')
def district(borough_type):
    borough = request.args.get('borough')
  
    f= open("Neighberhood_poverty.json", "r") 
    data = json.load(f)
    Borough_districts = list(data["Districts"])
    print("borough", Borough_districts)

    f.close()
    requestedData = {}
    for district in data['Districts']:
        for place in data['Districts'][district]:
             
             requestedData[place] = [round(float(data['Districts'][district][place]['percent']), 2)]
           
    colors = {}
    for i in range(1,11):
        colors[6 + i *(42 - 6)/10] = 100 - 10 * i

    
    for value in requestedData:
        for color in colors:
            if requestedData[value][0] < color:
                requestedData[value].append(colors[color])
                break

    return render_template('district.html',borough_type=borough_type, borough=borough, data=data, Borough_districts=Borough_districts, requestedData=requestedData)

@app.route('/borough')
def borough():
    f= open("Neighberhood_poverty.json", "r") 
    data = json.load(f)
    boroughs = list(data["borough"].keys())
    f.close()
    f= open("Neighberhood_poverty.json", "r") 
    data = json.load(f)
    Borough_districts = list(data["Districts"])
    print("borough", Borough_districts)
    requestedData = {}
    for borough in data['borough']:
        # Extract the place data, and check if 'percent' exists
        place_data = data['borough'][borough]
        if 'percent' in place_data:
            try:
                # Convert percent string to float, remove any commas or extra spaces
                percent_str = place_data['percent'].replace(',', '').strip()
                requestedData[borough] = [round(float(percent_str), 2)]
            except ValueError as e:
                print(f"Error converting percent value for {borough}: {e}")
                requestedData[borough] = [0]  # Default to 0 or another placeholder on error
        else:
            print(f"No 'percent' key found for {borough}")
            requestedData[borough] = [0]  # Handle the case where 'percent' key is missing

    # Color calculation 
    colors = {}
    for i in range(1, 11):
        colors[6 + i *(42 - 6)/10] = 100 - 10 * i

    # Assign colors based on the percentage values
    for value in requestedData:
        for color in colors:
            if requestedData[value][0] < color:
                requestedData[value].append(colors[color])
                break

    # Render the template with the necessary data
    return render_template('borough.html', data=data, boroughs=boroughs,  Borough_districts=Borough_districts,requestedData=requestedData)


app.run(debug=True)