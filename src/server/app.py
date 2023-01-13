from calendar import month_name
from flask import Flask, make_response, Response
from flask_cors import CORS
from src.server.errors import empty_data_error
from src.server.utils import games, get_all_critters, get_available_critters, get_monthly_critters


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/<game>/all", methods=["GET"])
def all(game: str) -> Response:
    """Return all critters for passed game."""
    assert game in games
    if res := get_all_critters(game):
        return make_response(res, 200)
    return make_response(empty_data_error, 500)

@app.route("/<game>/now", methods=["GET"])
def now(game: str) -> Response:
    """Return all critters available right now (month, time) for passed game."""
    assert game in games
    if res := get_available_critters(game):
        return make_response(res, 200)
    return make_response(empty_data_error, 500)

@app.route("/<game>/<month>", methods=["GET"])
def monthly(game: str, month: str) -> Response:
    """Return all critters available in passed month for passed game."""
    assert game in games
    assert month in [m for m in month_name][1:]
    if res := get_monthly_critters(game=game, month=month):
        return make_response(res, 200)
    return make_response(empty_data_error, 500)
