from Code.graph import graph
import csv
import os
import pandas as pd

"""
This file should be used for loading data from internet to the graph class.

Either through simply typing those data in or some other fancier ways, the
function to add nodes and edges would be implemented here!

"""

def load_data():
    covid_map = graph()
    sample = pd.read_csv("/Data/covid-19_cases_by_county--VA.csv")
    sample.head(10)
    print(sample[0])
def test():
    print("hello world")

load_data()