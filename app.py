from flask import Flask, request, jsonify

import meetup


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return ('Hey there!')


def handle_dialogflow_request(query):
    """Handle a webhook query from Dialogflow.

    Reference: https://dialogflow.com/docs/fulfillment

    Args:
        query (dict): Dialogflow webhook query.
    Returns:
        dict: Response that can be interpreted by Dialogflow.
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

    country = parameters['geo-country']

    groups = meetup.find_groups(country, 'machine learning')
    meetups = []
    for g in groups:
        new_meetups = meetup.get_upcoming_meetups_for_group(g['urlname'])
        if new_meetups:
            meetups.extend(new_meetups)

    # Sort meetups by date.
    meetups = sorted(meetups, key=lambda m: m['time'])

    response = {'fulfillmentText': 'some text',
                'fulfillmentMessages': [{'text': {'text': [m['name']]}}
                                        for m in meetups],
                'source': ''}

    return response


@app.route('/dialogflow', methods=['POST'])
def dialogflow_webhook():
    json_data = request.get_json()

    response = handle_dialogflow_request(json_data)
    json_response = jsonify(response)

    return json_response
