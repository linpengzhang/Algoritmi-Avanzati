import matplotlib.pyplot as plt

def draw_map(path, partenza, arrivo):
    # Read coordinates of the stations
    node_coords = read_station_coordinates()

    print("Drawing map...")
    plt.title("Tragitto del viaggio da " + partenza + " ad " + arrivo)
    plt.xlabel("Longitudine")
    plt.ylabel("Latitudine")
    for (lon, lat) in node_coords.values():
        plt.plot(lon, lat, marker='.', color='gray')
    
    # stampa percorso nella mappa
    for i in range(len(path)-1):
        from_station = path[i][0]
        to_station = path[i+1][0]
        # plot a line between the two stations
        plt.plot([node_coords[from_station][0], node_coords[to_station][0]], [node_coords[from_station][1], node_coords[to_station][1]], linestyle='-', color='blue')
    
    # plt.legend()
    print("Map created. Showing it...")
    plt.show()

def read_station_coordinates():
    """
    :return: List of coordinates of the stations
    """
    print("Reading coords from file...")
    file = open("./inputFiles/bfkoord", 'r', encoding="latin-1")
    node_coords = {}
    for row in file:
        station_number = row[0:9]
        if station_number.isalnum():
            longitude = float(row[12:20])
            latitude = float(row[22:30])
            node_coords[station_number] = (longitude, latitude)
    print("Coords read.")
    return node_coords