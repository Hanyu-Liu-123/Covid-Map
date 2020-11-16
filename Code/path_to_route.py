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


def test():
    print("hello world")



# turn_to_Google('https://www.google.com/maps/dir/Albemarle+County,+VA/Fairfax+County,+Virginia/Jefferson+Commons,+1620+Jefferson+Park+Ave,+Charlottesville,+VA+22903,+USA/Warren+County,+Virginia/')