import re
visits = dict()

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
    """Save places the user went to into the global var 'visits' """
    input_loop_active = True
    visits.clear()
    while input_loop_active:
        user_input = input("Tell me where you went: ")

        match_pattern = r'[\s]*(?P<city>[\s+\w]+),[\s]*(?P<country>[\w\s]+)[\s]*'
        valid_user_input = re.fullmatch(match_pattern, user_input)
        stop_input_loop = user_input.strip() == '' or user_input == '\n'

        if stop_input_loop:
            input_loop_active = False

        elif valid_user_input:
            city = valid_user_input.group('city')
            country = valid_user_input.group('country')

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