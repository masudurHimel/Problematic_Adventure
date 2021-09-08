data = {}
country = None


# main menu
def take_country(data_dict):
    country_input = input("Country: ")
    temp = data_dict.get(country_input, None)
    if temp is None:
        data_dict[country_input] = []
    return country_input


def take_olympian_input(data_dict, country):
    name = input("Name: ")
    medals = input("Medals: ")

    # validation check
    if name and medals and 0 <= int(medals) <= 35:
        data_dict[country].append((name, medals))
    else:
        if not medals or not name:
            print("Blank Entry")
        elif not 0 <= int(medals) <= 35:
            print("Incorrect Medal Entry")


def generate_report(data_dict):
    stat_dict = {}
    top_medal = []

    print("Results\n")
    print("-----------------------------")
    print("Olympic Medalists")

    for key in data_dict:
        temp_medals = 0
        for val in data_dict[key]:
            print(f"{val[0]}\t{key}\t{val[1]}")
            temp_medals = temp_medals + int(val[1])

        data_len = len(data_dict[key])
        average_medals = "{:.2f}".format(temp_medals / data_len)
        stat_dict[key] = (len(data_dict[key]), average_medals)

    print("-----------------------------")
    print("Country Statistics\n")
    for key in stat_dict:
        print(f"{key}\tTotal medalists = {stat_dict[key][0]}\tAverage = {stat_dict[key][1]}")

    print("-----------------------------")
    stat_sort = sorted(stat_dict.keys(), key=lambda x: stat_dict[x][1], reverse=True)
    print("And the winner is ")
    print(f"{stat_sort[0]} with {stat_dict[stat_sort[0]][1]} average medals")
    print("-----------------------------\n")


while True:

    if country is not None:
        print("Current Country: ", country)

    print("1: Enter Country")
    print("2: Enter Olympian Data")
    print("3: Generate Report")
    print("4: Export CSV")
    print("Q: Quit")
    print("--------------------------")
    option = input("Enter Your Choice [1/2/3/4/Q]: ")

    if option in ["Q", "q"]:
        break

    if option == "1":
        country = take_country(data)
        continue

    elif option == "2":
        take_olympian_input(data, country)
        continue

    elif option == "3":
        generate_report(data)

print(data)
