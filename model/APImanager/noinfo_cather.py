import datetime


def get_flight_callsign(details):
    try:
        return (details.get("identification"))['callsign']
    except (TypeError, AttributeError):
        return "No info"


def timstemp_to_human(stemp):
    raw_time = datetime.datetime.fromtimestamp(stemp)
    return raw_time.strftime("%H:%M")


def get_line_icao(details):
    try:
        return ((details.get("airline")).get('code'))['icao']
    except (TypeError, AttributeError):
        return "No info"


def get_line_name(details):
    try:
        return (details.get("airline")).get('name')
    except (TypeError, AttributeError):
        return "No info"


def get_departure_name(details):
    try:
        return ((details.get("airport")).get("origin"))['name']
    except (TypeError, AttributeError):
        return "No info"


def get_departure_icao(details):
    try:
        return ((details.get("airport")).get("origin")['code'])['icao']
    except (TypeError, AttributeError):
        return "No info"


def get_arrival_name(details):
    try:
        return (details.get("airport")).get("destination")['name']
    except (TypeError, AttributeError):
        return "No info"


def get_arrival_icao(details):
    try:
        return ((details.get("airport")).get("destination")['code'])['icao']
    except (TypeError, AttributeError):
        return "No info"


def get_model(details):
    try:
        return f'{details.get("aircraft").get("model").get("code")} {details.get("aircraft").get("model").get("text")}'
    except (TypeError, AttributeError):
        return "No info"


def get_time_departure(details):
    try:
        return timstemp_to_human(
            (details.get("time")).get("scheduled")['departure'])
    except (TypeError, AttributeError):
        return "No info"


def get_time_arrival(details):
    try:
        return timstemp_to_human(
            (details.get("time")).get("scheduled")['arrival'])
    except (TypeError, AttributeError):
        return "No info"
