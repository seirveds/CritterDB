from calendar import month_name
from typing import Union
from flask import Flask, make_response, Response
from flask_cors import CORS
from errors import empty_data_error
from utils import games, get_all_critters, get_filtered_critters


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/<game>/all", methods=["GET"])
@app.route("/<game>/all/<hemisphere>", methods=["GET"])
def all(game: str, hemisphere: str = 'n') -> Response:
    """Return all critters for passed game."""
    assert game in games
    assert hemisphere in ['n', 's']
    if res := get_all_critters(game, hemisphere):
        return make_response(res, 200)
    return make_response(empty_data_error, 500)


@app.route("/<game>/<month>", methods=["GET"])
@app.route("/<game>/<month>/<hemisphere>", methods=["GET"])
def month_available(game: str, month: str, hemisphere: str = 'n') -> Response:
    """Return all critters available in passed month and hour for passed game."""
    assert game in games
    assert month == 'now' or month in [m.lower() for m in month_name][1:]
    assert hemisphere in ['n', 's']

    if res := get_filtered_critters(game=game, month=month, hemisphere=hemisphere):
        return make_response(res, 200)
    return make_response(empty_data_error, 500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
