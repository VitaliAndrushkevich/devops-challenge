import json


def lambda_handler(event, context):
    try:
        if event.get('requestContext').get('http').get('method') == "GET":
            response = '''Welcome to our demo API, here are the details of your request:
Headers: {headers}
Method: {method}'''.format(
                headers=event.get('headers'),
                method=event.get('requestContext').get('http').get('method')
            )
        elif event.get('requestContext').get('http').get('method') == "POST":
            response = '''Welcome to our demo API, here are the details of your request:
Headers: {headers}
Method: {method} Body: {body}'''.format(
                headers=event.get('headers'),
                method=event.get('requestContext').get('http').get('method'),
                body=event.get('body')
                )
        else:
            response = "This method currently not supported"
    except Exception:
        response = "Make sure you send correct http request"
    return json.loads(json.dumps(response, default=str))
