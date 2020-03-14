import re

visits = {}

def display_places():
    """List all places the user visited"""
    global visits
    for country, cities in sorted(visits.items()):
        print(country)
        for cityname, visits in sorted(cities.items()):
            if visits['count'] > 1:
                print(f"\t{cityname} ({visits['count']})")
            else:
                print(f"\t{cityname}")

def collect_places():
    """Save places the user went into global var visits"""
    active = True
    while active:
        user_input = input("Tell me where you went: ")
        match_pattern = r'[\s]*([\s+\w]+),[\s]*([\w\s]+)[\s]*'
        user_input_regex_match = re.fullmatch(match_pattern,
                                              user_input)
        if user_input == '' or user_input == '\n':
            active = False
        elif user_input_regex_match:
            city = user_input_regex_match.group(1)
            country = user_input_regex_match.group(2)

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
    print(len(visits))
    display_places()