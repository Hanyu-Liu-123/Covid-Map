# CS4710 Project of Chengyuan Cai and Hanyu Liu
# See 'Paper Works' folder for more detail

import Code

covid_path = '/Users/hanyu/Desktop/Covid-Map/Data/united_states_covid19_cases_and_deaths_by_state.csv'
neigbor_path = '/Users/hanyu/Desktop/Covid-Map/Data/neighbor_states.csv'
position_path = '/Users/hanyu/Desktop/Covid-Map/Data/states.csv'

covid_map = Code.load_data_to_graph.load_data(covid_path, neigbor_path, position_path)

path = covid_map.dijkstra("Virginia", "Washington")

website = Code.path_to_route.path_to_Website(path)

Code.path_to_route.turn_to_Google(website)

print(path)

# Code.load_data_to_graph.test()
# Code.graph.test()
# Code.path_to_route.test()
