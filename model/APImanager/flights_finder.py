from FlightRadar24.api import FlightRadar24API
from geopy.geocoders import Nominatim
from model.APImanager import noinfo_cather as cat


class Picker:
    # (pseudo)private variables because they are not used outside

    __fr24 = FlightRadar24API()  # initialization of API
    __geoflag = False
    flight_detailed = []
    __lat = 0.0
    __long = 0.0

    # ------------------ arent used in the actual process, made for educationas purposes -------------------------------
    def __str__(self):
        tmp = {}
        count = [i for i in range(len(self.flight_detailed))]
        i = 0
        for details in self.flight_detailed:
            tmp.update({count[i]: list(details.values())})
            i += 1

        res = '\n'.join(str(item) for item in tmp.items())
        return res

    def __len__(self):
        return len(self.flight_detailed)

    # ------------------------------------------------------------------------------------------------------------------

    # pseudo private method, which is made to find the position based on the location name
    def _get_my_pos(self, name):
        loc = Nominatim(user_agent="Get Loc")
        location_name = loc.geocode(name)
        self.__lat = float(location_name.latitude)
        self.__long = float(location_name.longitude)

    # method which actually scans the provided radius around the provided area
    def get_by_bounds(self, rad, name):
        self.flight_detailed = []
        if not self.__geoflag:
            self._get_my_pos(name)

        # translates the center of the improvised circle and the radius into the Flight Radar bounds set
        bounds = self.__fr24.get_bounds_by_point(self.__lat, self.__long, float(rad * 1000))
        flights = self.__fr24.get_flights(bounds=bounds) # gets flights info

        # since each flight contains alot of data, each flight gets parsed and the valuable information gets pulled from
        # it and aprsed flights are stored in the list of dicts

        # p.s. each inforamtion retrivement is secured by noinfo catcer module

        if len(flights) != 0:
            count = 1
            for flight in flights:
                current_flight = self.__fr24.get_flight_details(flight)
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
