def convert2int(a):
    try:
        x = int(a)
        return x
    except ValueError:
        return -1


def add_segment(cityB, distance, limit, highway):
    return Segment(cityB, distance, limit, highway)


class Segment:

    def __init__(self, city, distance, limit, highway):
        self.city = city
        self.distance = convert2int(distance)
        self.limit = convert2int(limit)
        self.highway = highway


class City:

    def __init__(self, name, latitude=0, longitude=0):
        self.name = name
        self.lat = latitude
        self.long = longitude

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name
