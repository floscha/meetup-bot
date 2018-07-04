import os

import requests


DIALOGFLOW_API_URL = 'https://api.dialogflow.com/v1/query?v=20150910'


def post_query(session_id, query, language='en', timezone='America/New_York'):
    """Post a query to the Dialogflow API.

    Reference: https://dialogflow.com/docs/reference/agent/query
    """
    dialogflow_client_token = os.environ['DIALOGFLOW_CLIENT_TOKEN']
    r = requests.post(DIALOGFLOW_API_URL,
                      headers={'Authorization': 'Bearer '
                                                + dialogflow_client_token,
                               'Content-Type': 'application/json'},
                      json={'sessionId': session_id,
                            'query': query,
                            'lang': language,
                            'timezone': timezone})
    json_data = r.json()
    return json_data


def main():
    session_id = '12345'
    query = 'find machine learning meetups in switzerland'
    json_data = post_query(session_id, query)

    import pprint
    pprint.pprint(json_data)


if __name__ == '__main__':
    main()
