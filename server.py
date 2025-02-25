from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

scoreboard = [
    {
    "id": 1,
    "name": "Boston Bruins",
    "score": 7
    },

    {
    "id": 2,
    "name": "Tampa Bay Lightning", 
    "score": 5
    },

    {
    "id": 3,
    "name": "Toronto Maple Leafs", 
    "score": 2
    },

    {
    "id": 4,
    "name": "Florida Panthers", 
    "score": 1
    },

    {
    "id": 5,
    "name": "Buffalo Sabres", 
    "score": 1
    },
]


@app.route('/')
def show_scoreboard():
    global scoreboard
    return render_template('scoreboard.html', scoreboard = scoreboard) 

@app.route('/increase_score', methods=['GET', 'POST'])
def increase_score():
    global scoreboard

    json_data = request.get_json()   
    team_id = json_data["id"]  
    
    for i in range(len(scoreboard)):
        if scoreboard[i]["id"] == team_id:
            scoreboard[i]["score"] += 1

        # Adding sort condition
        if i > 0 and scoreboard[i-1]["score"] < scoreboard[i]["score"]:
            scoreboard[i], scoreboard[i-1] = scoreboard[i-1], scoreboard[i]

    return jsonify(scoreboard=scoreboard)


if __name__ == '__main__':
   app.run(debug = True)




