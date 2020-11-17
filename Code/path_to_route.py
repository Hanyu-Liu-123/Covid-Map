import webbrowser

"""
This file should be used for generating a user-friendly representation of route from solutions
returned by find_optimal_path.py

Note here GoogleMap is a good option.

https://www.google.com/maps/dir/Albemarle+County,+VA/Fairfax+County,+Virginia/Jefferson+Commons,+1620+Jefferson+Park+Ave,+Charlottesville,+VA+22903,+USA/Warren+County, +Virginia/

We can generate a website link by adding "(County Name)+Country,+(State)/" to the prefix https://www.google.com/maps/dir/
"""


def turn_to_Google(website):
    """
    this function opens the given website in the default browser
    """

    new = 1
    url = website
    webbrowser.open(url, new=new)


def path_to_Website(city_list):
    """
    this function takes in a list of cities and return a google map link that can be viewed by a browser
    """
    link_prefix = "https://www.google.com/maps/dir/"

    for city in city_list:
        addition = city.replace(" ", "+")
        addition += "/"
        link_prefix += addition

    return link_prefix


def test():
    print("hello world")
    list = []
    list.append("Albemarle County, Virginia")
    list.append("Warren County, Virginia")
    list.append("Orange County, California")
    list = list*5
    print(path_to_Website(list))
    turn_to_Google(path_to_Website(list))