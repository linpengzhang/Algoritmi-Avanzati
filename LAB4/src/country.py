class Dataset:
    """
    Represents a list of countries
    """

    def __init__(self, filename=None):
        self.dataset = []
        if filename is not None:
            file = open(filename, 'r')
            for row in file:
                self.dataset.append(Country(row.split(',')))
            file.close()

    def append(self, c):
        self.dataset.append(c)

    def get_list_of_coords(self):
        return list(map(lambda c : c.get_coords() , self.dataset))


class Country:
    """
    Represents a single country
    """

    def __init__(self, parameters):
        self.country_id = parameters[0]
        self.x = float(parameters[1])
        self.y = float(parameters[2])
        self.population = int(parameters[3])
        self.cancer_risk = float(parameters[4])

    def get_coords(self):
        return (self.x, self.y)