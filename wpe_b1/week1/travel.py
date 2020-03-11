import re
from collections import OrderedDict

visits = OrderedDict()

def display_places():
    """List all places the user visited"""
    global visits
    for country, cities in visits.items():
        print(country)
        for cityname, visits in cities.items():
            if visits['count'] > 1:
                print(f"\t{cityname} ({visits['count']})")
            else:
                print(f"\t{cityname}")

def collect_places():
    """Save places the user went into global var visits"""
    active = True
    while active:
        user_input = input("Tell me where you went: ")
        user_input_format_valid = re.fullmatch(r'[\s\w]+,[\s]*[\w\s]+', user_input)

        if user_input == '':
            active = False
        elif user_input_format_valid:
            city, country = user_input.split(',')
            if country in visits:
                if city in visits[country]:
                    visits[country][city]['count'] += 1
                else:
                    visits[country][city] = {"count": 1}
            else:
                visits[country] = {city: {"count": 1}}
        else:
            print("That's not a legal city, country combination")

if __name__ == "__main__":
    collect_places()
    display_places()