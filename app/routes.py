from app import app
from flask import render_template
@app.route("/")
@app.route("/home")
def home():
    player_info = [{
        'name' : 'micheal jordan',
        'age' : 30,
        'team': 'chicgo'
        }]
    
    return render_template('index.html', info=player_info)

@app.route("/players")
def players():
    favorit_player = ['micheal Jordan', 'koby bryant', 'stephen curry', 'tracy mcgrady', 'reggie miller']
    return render_template('players.html', names=favorit_player)