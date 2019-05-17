class Dataset:

    def __init__(self, filename):
        file = open(filename, 'r')
        self.dataset = []
        for row in file:
            self.dataset.append(Country(row.split(',')))
        file.close()

    def get_coords(self):
        return list(map(lambda c : (c.x, c.y) , self.dataset))


class Country:

    def __init__(self, parameters):
        self.country_id = parameters[0]
        self.x = float(parameters[1])
        self.y = float(parameters[2])
        self.population = int(parameters[3])
        self.cancer_risk = float(parameters[4])