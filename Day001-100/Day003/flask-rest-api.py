from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test_get():
    return jsonify(result="To jest GET!")


@app.route('/test', methods=['POST'])
def test_post():
    # request_data = request.get_json()
    # return request_data
    city = request.args.get('city')
    return jsonify(city=city)


app.run(port=8000)
