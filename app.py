from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return ('Hey there!')


@app.route('/dialogflow', methods=['POST'])
def dialogflow_webhook():
    json_data = request.get_json()
    query_result = json_data['queryResult']

    # String	The original text of the query.
    query_text = query_result['queryText']
    # Object	Consists of parameter_name:parameter_value pairs.
    parameters = query_result['parameters']
    # Object	The intent that matched the user's query.
    intent = query_result['intent']
    # Number 0-1	Matching score for the intent.
    detection_confidence = query_result['intentDetectionConfidence']
    # String	The language that was triggered during intent matching.
    intent_language = query_result['languageCode']

    response = {'fulfillmentText': 'some text',
                'fulfillmentMessages': [{'text': {'text': [str(query_result)]}}],
                'source': ''}
    json_response = jsonify(response)

    return json_response
