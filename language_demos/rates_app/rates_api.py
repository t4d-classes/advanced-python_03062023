from typing import Any
import math
import pathlib
import time
from flask import Flask, Response, request, jsonify, abort

from rates_data import load_rates_from_history


rates: list[dict[str,Any]] = []

app = Flask(__name__)

@app.route("/check")
def check() -> Response:
    """ health check endpoint """
    return "READY"


@app.route("/api/<rate_date>")
def rates_by_date(rate_date: str) -> Response:
    """ rates_by_date """

    # time.sleep(1)

    for rate in rates:

        if rate["Date"] == rate_date:

            base_country = request.args.get("base", "EUR")

            if "symbols" in request.args:
                country_symbols = request.args["symbols"].split(",")
            else:
                country_symbols = [ col for col in rate if col != "Date" ]

            country_rates = {
                country_code: country_rate / rate[base_country]
                for (country_code, country_rate) in rate.items()
                if country_code != "Date" and
                country_code in country_symbols and
                not math.isnan(country_rate)
            }

            return jsonify({
                "date": rate["Date"],
                "base": base_country,
                "rates": country_rates
            })

    abort(404)


def start_rates_api() -> None:
    """ start rates api """

    # rates is not declared in this function,
    # the statement below is assignment only
    global rates

    rates_file_path = pathlib.Path("../data/eurofxref-hist.csv")

    rates = load_rates_from_history(rates_file_path)

    app.run(port=5050)


if __name__ == "__main__":
    start_rates_api()