# WallE Algorithm

## Problem Statement
Assume Wall-E is a robot programmed to walk along a circular road. 
Although Wall-E has a battery with unlimited capacity, his battery is dead at the onset of his travel. 
There are n charging stations along the road. 

The ith charging station can provide charge[i] capacity for Wall-E’s battery. 
Each trip from ith station to the next station ( i + 1th) consumes cost[i] of battery.

Given n and the two length-n arrays charge[i] and cost[i] 
(listed in clockwise order starting from station 0) for circular road C, 
propose an efficient algorithm to help the programmers to know:

• If Wall-E can walk the whole road C clockwise.
• If yes, which charging station(s) can be the starting point.

Obviously, one can do this in O(n^2) time. Your task is to do better. 

## Notes from Discussion 
For Problem 4 of Assignment 2, please assume that there is only one valid solution.
This way, you could reach a time complexity less than O(n^2).

Andy's Interpretation: Return 1 charging station that can be the starting point. 

## Inputs 
n = Int: Number of Charging Stations 
charge[] = Array: charge[i] is equal to the energy WallE charges from station i. 
trip[] = Array: trip[i] is equal to the energy WallE uses to travel from station i to i+1.

## Outputs 
walkable = Bool: Can WallE walk the road
station = Int: Starting Station Number


# Algorithm 

## Lemma 1: Sum of Charges must be greater than Sum of Road Consumption
For WallE to travel a road R of Cost A, WallE must have a Charge B >= Cost A. 
If Charge B < Cost A, WallE cannot travel road R. 
The road R has now been split into multiple Stations S = (S1, S2 ... Sn) and Roads R = (R1, R2 ... Rn)
To travel the Road R, WallE must gain a total charge of TotalCharge >= TotalCostR. 
Since WallE only charges at Stations, and starts at zero, TotalStationCharge >= TotalCostR. 
Aka, Sum S >= Sum R

## Lemma 2: A Station Exists with a greater Charge than next Road Consumption 
Stations S = (S1, S2 ... Sn) and Roads R = (R1, R2 ... Rn)
S1 < R1 and S2 < R2 ... Sn < Rn is not possible, because then Sum S < Sum R, 
which contradicts Lemma 1
Therefore, at least 1 Si >= Ri

## Solution: Add Cant Con't Paths to Can Cont Paths, until there are only Can Cont Paths. 
Combine All Sa < Ra with Sb > Rb, until there are no more Si < Ri. 
This will happen, because there always exists a Si > Sj by Lemma 2. 
When there are no more Si < Ri, all stations left can travel the road ahead, 
meaning that any station remaining will be a valid station to start with. 

Why the Algorithm works, and why the while loop is done twice. 
Starting from the end of the loop, we get rid of each station which is not walkable, by adding it to the previous station. 
This creates a road that is comprised of two roads. If the road turns out to now be walkable, we move on, and if not, we combine this again with the next station. By eliminating all unwalkable roads, we will be left with 2 scenarios. 
Either we have all walkable roads, or we have the last road combine with the first road. The first road is now unwalkable, and all other stations are walkable. We have 1 unwalkable road left. So, we must do one final loop to get rid of this unwalkable road. 
We keep on combining this one unwalkable road until it is combined to form a walkable road. We know this must happen because Sum of S is greater than Sum of R. 


# Pseudo Code 
# Stations = number of stations 
# Charges = Array of charges for each station
# Costs = Array of Costs from station i to j
walle algorithm(stations, charges, costs) 
    if sum(charges) < sum(costs)
        return not possible
    else 
        road [] # Array of [station name, charge, cost, walkable]

        for station = 0 to stations:
            if charges[station] >= trips[station]:
                road.append([station, charges[station], trips[station], True])
            else:
                road.append([station, charges[station], trips[station], False])
        
        for i in range 2:
            current_station = len(road) - 1 # end of the circle. 
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

        return road[0][STATION_NAME] # can be any station in road. 