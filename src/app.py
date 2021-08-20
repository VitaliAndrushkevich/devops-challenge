#!/usr/bin/python3


class IncorrectRequest(Exception):
    pass


def get_method(event):
    try:
        # method = event.get("requestContext").get("http").get("method")
        method = event.get('httpMethod')
    except AttributeError:
        return "Not valid query format"
    if method in ("POST", "GET"):
        return method
    else:
        raise IncorrectRequest("This request method currently unavaliable.")


def get_headers(event):
    try:
        return event.get("headers")
    except AttributeError:
        return "Not valid query format"


def get_body(event, method):
    try:
        return event.get("body") if method == "POST" else None
    except AttributeError:
        return "Not valid query format"


def lambda_handler(event, context):
    w_str = "Welcome to our demo API, here are the details of your request:"

    try:
        method = get_method(event)
        headers = get_headers(event)
        body = get_body(event, method)
    except IncorrectRequest as ex:
        return str(ex)

    if method == "GET":
        return "\n".join((w_str, f"Headers: {headers}", f"Method: {method}"))
    elif method == "POST":
        return "\n".join(
            (w_str, f"Headers: {headers}", f"Method: {method} Body: {body}")
        )
    return "This request method currently unavaliable."
