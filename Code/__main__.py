# CS4710 Project of Chengyuan Cai and Hanyu Liu
# See 'Paper Works' folder for more detail

import Code
import time

"""
User Interface
"""

covid_path = '/Users/hanyu/Desktop/Covid-Map/Data/united_states_covid19_cases_and_deaths_by_state.csv'
neigbor_path = '/Users/hanyu/Desktop/Covid-Map/Data/neighbor_states.csv'
position_path = '/Users/hanyu/Desktop/Covid-Map/Data/states.csv'

print()
print("******************************** Welcome to COVID-MAP ********************************\n")

while True:
    weight_distance = int(input("How much do you value a faster route? Enter a number between 1 and 100: "))
    if weight_distance <= 1:
        weight_distance = 1
    weight_safety = int(input("How much do you value a safer route? Enter a number between 1 and 100: "))
    if weight_safety <= 1:
        weight_safety = 1
    print()

    covid_map = Code.load_data_to_graph.load_data(covid_path, neigbor_path, position_path, weight_distance,
                                                  weight_safety)

    start = input("Enter the state you'll start in: ")
    end = input("Enter the state you want to go: ")
    print()

    while True:
        search_algo = input("Enter A to use dijkstra, B to use bfs, and C to use dfs: ")
        if search_algo == "A":
            path = covid_map.dijkstra(start, end)
            break
        elif search_algo == "B":
            path = covid_map.bfs(start, end)
            break
        elif search_algo == "C":
            path = covid_map.dfs(start, end)
            break
        else:
            continue
    print()

    print("Figuring out the path....\n")
    # time.sleep(2)

    if path is None:
        print("No path available, sorry :(")
    else:
        print("Your optimal path is:")
        num = 1
        while num <= len(path):
            print(f"{num}. {path[num - 1]}")
            num += 1

        print()
        print("Switching to Google Maps in 5 seconds.....")
        time.sleep(5)

        website = Code.path_to_route.path_to_Website(path)
        Code.path_to_route.turn_to_Google(website)

    print()
    again = input("Enter 'q' to quit, or any other key to calculate another route: \n")
    if again == 'q':
        break




# Code.load_data_to_graph.test()
# Code.graph.test()
# Code.path_to_route.test()
