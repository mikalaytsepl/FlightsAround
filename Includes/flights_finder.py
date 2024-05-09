from FlightRadar24.api import FlightRadar24API
from geopy.geocoders import Nominatim
import datetime


class Parser:

    def _get_flight_callsign(self, details):
        try:
            return (details.get("identification"))['callsign']
        except (TypeError, AttributeError):
            return "No info"

    def _timstemp_to_human(self, stemp):
        raw_time = datetime.datetime.fromtimestamp(stemp)
        return raw_time.strftime("%H:%M")

    def _get_line_icao(self, details):
        try:
            return ((details.get("airline")).get('code'))['icao']
        except (TypeError, AttributeError):
            return "No info"

    def _get_line_name(self, details):
        try:
            return (details.get("airline")).get('name')
        except (TypeError, AttributeError):
            return "No info"

    def _get_departure_name(self, details):
        try:
            return ((details.get("airport")).get("origin"))['name']
        except (TypeError, AttributeError):
            return "No info"

    def _get_departure_icao(self, details):
        try:
            return ((details.get("airport")).get("origin")['code'])['icao']
        except (TypeError, AttributeError):
            return "No info"

    def _get_arrival_name(self, details):
        try:
            return (details.get("airport")).get("destination")['name']
        except (TypeError, AttributeError):
            return "No info"

    def _get_arrival_icao(self, details):
        try:
            return ((details.get("airport")).get("destination")['code'])['icao']
        except (TypeError, AttributeError):
            return "No info"

    def _get_model(self, details):
        try:
            return f'{details.get("aircraft").get("model").get("code")} {details.get("aircraft").get("model").get("text")}'
        except (TypeError, AttributeError):
            return "No info"

    def _get_time_departure(self, details):
        try:
            return self._timstemp_to_human(
                (details.get("time")).get("scheduled")['departure'])
        except (TypeError, AttributeError):
            return "No info"

    def _get_time_arrival(self, details):
        try:
            return self._timstemp_to_human(
                (details.get("time")).get("scheduled")['arrival'])
        except (TypeError, AttributeError):
            return "No info"


class Picker(Parser):
    country_boundaries = {}
    fr24 = FlightRadar24API()
    geoflag = False
    allflightinfo = []
    flight_detailed = []
    lat = 0.0
    long = 0.0

    def _get_my_pos(self, name):
        loc = Nominatim(user_agent="Get Loc")
        location_name = loc.geocode(name)
        self.lat = float(location_name.latitude)
        self.long = float(location_name.longitude)

    def get_by_bounds(self, rad, name):
        self.flight_detailed = []
        if not self.geoflag:
            self._get_my_pos(name)

        bounds = self.fr24.get_bounds_by_point(self.lat, self.long, float(rad * 1000))
        flights = self.fr24.get_flights(bounds=bounds)
        if len(flights) != 0:
            count = 1
            for flight in flights:
                current_flight = self.fr24.get_flight_details(flight)
                self.flight_detailed.append(
                    {"callsing": self._get_flight_callsign(current_flight),
                     "line": self._get_line_name(current_flight),
                     "icao": self._get_line_icao(current_flight),
                     "model": self._get_model(current_flight),
                     "departure_name": self._get_departure_name(current_flight),
                     "departure_icao": self._get_departure_icao(current_flight),
                     'time_departure': self._get_time_departure(current_flight),
                     "arrival_name": self._get_arrival_name(current_flight),
                     "arrival_icao": self._get_arrival_icao(current_flight),
                     'time_arrival': self._get_time_arrival(current_flight)
                     })
                count += 1
