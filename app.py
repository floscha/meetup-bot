from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return ('Hey there!')


@app.route('/dialogflow', methods=['POST'])
def dialogflow_webhook():
    payload = request.get_json()

    print(payload)

    response = {'fulfillmentText': 'some text',
                'fulfillmentMessages': [{'text': {'text': ['some text']}}],
                'source': ''}
    json_response = jsonify(response)

    return json_response
