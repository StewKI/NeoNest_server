import os
from pyngrok import ngrok
from secret import ngrok_token
ngrok.set_auth_token(ngrok_token)

from open_api import prompt

from flask import Flask, jsonify
from ha_api import get_current

app = Flask(__name__)

rooms = [
        'kitchen', 'open_space', 'office_box', 'working_space_1', "working_space_2"
    ]

def get_score(x):
    y = -((x/150.0)**2) + 100
    print(y)
    if y > 100:
        y = 100
    elif y < 0:
        y = 0
    
    return int(y)


@app.route('/rooms')
def get_rooms():
    data = {'rooms': rooms}
    return jsonify(data)

@app.route('/room/<index>')
def get_room(index):
    i = int(index)
    co = get_current(rooms[i], "co2_ppm")
    rh = get_current(rooms[i], "atmospheric_pressure")
    press = get_current(rooms[i], "relative_humidity")
    temp = get_current(rooms[i], "temperature")
    msg = prompt(co, rh, press, temp)
    newScore = get_score(co)
    data = {
        'score' : newScore,
        'messages' : [
            msg
        ]
    }
    
    return jsonify(data)

# Start ngrok to tunnel the local server
public_url = ngrok.connect(5000)
print(f'Public URL: {public_url}')

app.run(port=5000)