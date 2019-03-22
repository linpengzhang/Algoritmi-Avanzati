class Route:
    def __init__(self, time_departure=0, time_arrival=0, route_uid=""):
        self.time_departure = time_departure
        self.time_arrival = time_arrival
        self.route_uid = route_uid

    def __str__(self):
        return '(' + str(self.time_departure) + ', ' + str(self.time_arrival) + ', ' + str(self.route_uid) + ')'

    def __repr__(self):
        return '(' + str(self.time_departure) + ', ' + str(self.time_arrival) + ', ' + str(self.route_uid) + ')'
