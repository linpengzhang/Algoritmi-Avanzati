class Dataset:
    """
    Represents a list of countries
    """

    def __init__(self, lista):
        self.dataset = lista

    @classmethod
    def read_from_file(cls, filename):
        file = open(filename, 'r')
        lista = []
        for row in file:
            lista.append(County(row.split(',')))
        file.close()
        return cls(lista)

    def append(self, c):
        self.dataset.append(c)

    def get_coords(self):
        return list(zip(*[c.get_coords() for c in self.dataset]))

    def __str__(self):
        return str(len(self.dataset))
        
    def __repr__(self):
        return str(len(self.dataset))
class County:
    """
    Represents a single county
    """

    def __init__(self, parameters):
        self.country_id = parameters[0]
        self.x = float(parameters[1])
        self.y = float(parameters[2])
        self.population = int(parameters[3])
        self.cancer_risk = float(parameters[4])

    def get_coords(self):
        return self.x, self.y
