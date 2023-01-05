from flask import Flask, make_response
from flask_cors import CORS
from src.server.errors import empty_data_error
from src.server.utils import games, get_all_critters, get_available_critters


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/all/<game>", methods=["GET"])
def all(game):
    assert game in games
    if res := get_all_critters(game):
        return make_response(res, 200)
    return make_response(empty_data_error, 500)

@app.route("/now/<game>", methods=["GET"])
def now(game):
    assert game in games
    if res := get_available_critters(game):
        return make_response(res, 200)
    return make_response(empty_data_error, 500)
