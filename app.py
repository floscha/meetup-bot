from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return ('Hey there!')


def handle_dialogflow_request(query):
    """Handle a webhook query from Dialogflow.
    
    Reference: https://dialogflow.com/docs/fulfillment

    Args:
        query (dict): Dialogflow webhook query.

    """
    query_result = query['queryResult']

    # String: The original text of the query.
    query_text = query_result['queryText']
    # Object: Consists of parameter_name:parameter_value pairs.
    parameters = query_result['parameters']
    # Object: The intent that matched the user's query.
    intent = query_result['intent']
    # Number 0-1: Matching score for the intent.
    detection_confidence = query_result['intentDetectionConfidence']
    # String: The language that was triggered during intent matching.
    intent_language = query_result['languageCode']

    response = {'fulfillmentText': 'some text',
                'fulfillmentMessages': [{'text': {'text': [str(query_result)]}}],
                'source': ''}


@app.route('/dialogflow', methods=['POST'])
def dialogflow_webhook():
    json_data = request.get_json()

    response = handle_dialogflow_request(json_data)
    json_response = jsonify(response)

    return json_response
