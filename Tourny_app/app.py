from flask import Flask, render_template

from controllers.player_controller import player_blueprint
from controllers.match_controller import match_blueprint


app = Flask(__name__)

app.register_blueprint(player_blueprint)
app.register_blueprint(match_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)