FILE = "e.txt"

def is_road_walkable(charges, costs):
    total_charge = sum(charges)
    total_trip_cost = sum(costs)
    return total_charge >= total_trip_cost

def getInputs():
    input_file = open(FILE, "r")

    stations_line = input_file.readline()
    stations = int(stations_line)

    charges_line = input_file.readline()
    charges = list(map(int, charges_line.split()))

    costs_line = input_file.readline()
    costs = list(map(int, costs_line.split()))

    return (stations, charges, costs)

def find_valid_station(stations, charges, trips):   
    road = [] # Array of [station name, charge, cost, walkable]
    STATION_NAME = 0  
    CHARGE = 1
    COST = 2
    WALKABLE = 3 # Walkable if Charge >= Cost

    # initialize road 
    for station in range(stations):
        if charges[station] >= trips[station]:
            road.append([station, charges[station], trips[station], True])
        else:
            road.append([station, charges[station], trips[station], False])
    print("Road: ", road)

    for i in range(2):
        current_station = len(road) - 1
        while current_station != -1:
            if road[current_station][WALKABLE] == True:
                current_station -= 1 # Walkable, so move to next station
            else: 
                # road current station not walkable
                next_station = (current_station - 1) % len(road)

                # combine current station with next station
                road[next_station][CHARGE] += road[current_station][CHARGE]
                road[next_station][COST] += road[current_station][COST]
                road[next_station][WALKABLE] = (road[next_station][CHARGE] >= road[next_station][COST])

                # delete current station
                road.pop(current_station)
                current_station -= 1
                # current station now points at the newly combined station
        print(road)        

    return road[0][STATION_NAME] # can be any station in road. 


def main():
    (stations, charges, costs) = getInputs()

    if is_road_walkable(charges, costs):
        print("Road Walkable")
        print(find_valid_station(stations, charges, costs))
    else:
        print("Road not Walkable")

main()
    