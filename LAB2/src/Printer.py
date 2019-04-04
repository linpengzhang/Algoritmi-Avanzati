from datetime import time


def print_solution(partenza, arrivo, path):
    print(" *** SOLUZIONE TROVATA: *** ")
    print("Viaggio da", partenza, "a", arrivo)

    # path: lista di tuple (stazione, possible corsa successiva, ora di arrivo) che compone il percorso
    if len(path) > 0:
        print("Orario di partenza:", print_time(path[0][2]))
        print("Orario di arrivo:", print_time(path[len(path) - 1][2]))
        idx_from = 0  # indice del percorso della partenza di una corsa
        idx_to = 1  # indice del percorso dell'arrivo di una corsa
        while idx_to < len(path):
            current_route = path[idx_from][1].route_uid  # uid corsa dell'arco attualmente considerato
            # finché nel percorso continuo con la stessa corsa, ignoro le stazioni intermedie
            while idx_to < len(path) - 1 and current_route == path[idx_to][1].route_uid:
                idx_to += 1
            # stampo le informazioni di una corsa che compone il percorso
            t_departure = print_time(
                path[idx_from][1].time_departure)  # orario di partenza dalla prima stazione della corsa considerata
            t_arrival = print_time(
                path[idx_to - 1][1].time_arrival)  # orario di arrivo all'ultima stazione della corsa considerata
            print(t_departure, "->", t_arrival, ": corsa", current_route, "da", path[idx_from][0], "a", path[idx_to][0])
            # aggiorno gli indici relativi alle stazioni considerate nel percorso
            idx_from = idx_to
            idx_to = idx_from + 1
    else:
        print("Non c'è nessun viaggio che soddisfa i vincoli richiesti")


def print_time(t):
    """
    :return: Returns a string representing the time in the format HH:MM
    """
    return time(t // 100 % 24, t % 100).strftime("%H:%M") + (
        "" if t < 2400 else (" (" + str(t // 2400) + " giorno/i dopo)"))
