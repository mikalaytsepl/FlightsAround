from FlightRadar24.api import FlightRadar24API
from geopy.geocoders import Nominatim
from Includes import noinfo_cather as cat


class Picker:
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
                    {"callsing": cat.get_flight_callsign(current_flight),
                     "line": cat.get_line_name(current_flight),
                     "icao": cat.get_line_icao(current_flight),
                     "model": cat.get_model(current_flight),
                     "departure_name": cat.get_departure_name(current_flight),
                     "departure_icao": cat.get_departure_icao(current_flight),
                     'time_departure': cat.get_time_departure(current_flight),
                     "arrival_name": cat.get_arrival_name(current_flight),
                     "arrival_icao": cat.get_arrival_icao(current_flight),
                     'time_arrival': cat.get_time_arrival(current_flight)
                     })
                count += 1
