# -*- coding: utf-8 -*-

import json
import requests
from flask import abort, Flask, make_response, Response

app = Flask(__name__)

@app.route("/api/v1/cambio/<string:fr>/<string:to>", methods=["GET"])
def cambio(fr, to):
    url = "https://free.currencyconverterapi.com/api/v6/convert?q={0}_{1}&compact".format(fr.upper(), to.upper())
    key = "{0}_{1}".format(fr.upper(), to.upper())
    res = requests.get(url)
    data = json.loads(res.content)
    
    if data.get("query").get("count") >= 1:
        return make_response("resultado: {0}".format(
            round(data["results"][key]["val"], 2)) , 200)
    else:
        abort(Response(
            "Não foi possível fazer a conversão das moedas informadas!"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=False)
