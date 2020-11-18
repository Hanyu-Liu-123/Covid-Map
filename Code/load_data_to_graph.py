from Code.graph import graph
import csv
import math

"""
This file should be used for loading data from internet to the graph class.

Either through simply typing those data in or some other fancier ways, the
function to add nodes and edges would be implemented here!

data from 
1. https://state.1keydata.com/bordering-states-list.php
2. https://www.vdh.virginia.gov/coronavirus/
3. https://gist.github.com/rozanecm/29926a7c8132a0a25e3b12a24abdff86#file-states-csv


"""


def load_data(covid_path, neighbor_path, position_path, weight_distance=1, weight_safety=1):

    covid_map = graph()
    covid_cases_by_location = {}
    state_position = {}
    state_distance = {}
    weight_safety = weight_safety / (weight_safety+weight_distance)
    weight_distance = weight_distance / (weight_safety+weight_distance)

    # load cities as nodes to the graph
    # load covid cases to covid_cases_by_location and then normalize
    max = 0
    with open(covid_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            temp = row[0].split()
            location = ""
            for x in temp:
                location += x.capitalize() + " "
            location = location[:len(location)-1]

            cov_cases_per_100k = float(row[11])
            if max < cov_cases_per_100k:
                max = cov_cases_per_100k
            covid_cases_by_location[location] = cov_cases_per_100k
            covid_map.add_node(f"{location}")

        for location in covid_cases_by_location.keys():
            # normalize
            covid_cases_by_location[location] = covid_cases_by_location[location] / max
            # print(location, covid_cases_by_location[location])

    # load positions of states to state_position
    with open(position_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            state_position[row[0]] = (float(row[1]), float(row[2]))

    # load edges raw data into state_position
    max = 0
    with open(neighbor_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            location = row[0]
            if location not in state_position.keys() or location not in covid_cases_by_location.keys():
                raise ValueError("Incomplete data")
            for neighbor_state in row[1:]:
                if neighbor_state == "None":
                    continue
                else:
                    location_pos = state_position[location]
                    neighbor_pos = state_position[neighbor_state]
                    state_distance[(location, neighbor_state)] = distance_between(location_pos, neighbor_pos)
                    #print(location, neighbor_state, state_distance[(location, neighbor_state)])

                    if max < state_distance[(location, neighbor_state)]:
                        max = state_distance[(location, neighbor_state)]

        for key in state_distance.keys():
            # normalize
            state_distance[key] = state_distance[key] / max
            state1 = key[0]
            state2 = key[1]
            safety_cost1 = covid_cases_by_location[state2] / covid_cases_by_location[state1] * weight_safety
            safety_cost2 = covid_cases_by_location[state1] / covid_cases_by_location[state2] * weight_safety
            edge_cost1 = weight_distance * state_distance[key] + safety_cost1
            edge_cost2 = weight_distance * state_distance[key] + safety_cost2
            # print(state1, state2, covid_cases_by_location[state1], covid_cases_by_location[state2], state_distance[key])
            covid_map.add_edge(state1, state2, edge_cost1, edge_cost2)

    # print(covid_map)
    return covid_map


def distance_between(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return math.sqrt(x*x + y*y)


def test():
    covid_path = '/Users/hanyu/Desktop/Covid-Map/Data/united_states_covid19_cases_and_deaths_by_state.csv'
    neigbor_path = '/Users/hanyu/Desktop/Covid-Map/Data/neighbor_states.csv'
    position_path = '/Users/hanyu/Desktop/Covid-Map/Data/states.csv'
    load_data(covid_path, neigbor_path, position_path)
