import csv

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
    return stat_dict


def generate_report_result_only(data_dict):
    stat_dict = {}
    for key in data_dict:
        temp_medals = 0
        for val in data_dict[key]:
            temp_medals = temp_medals + int(val[1])

        data_len = len(data_dict[key])
        average_medals = "{:.2f}".format(temp_medals / data_len)
        stat_dict[key] = (len(data_dict[key]), average_medals)

    stat_sort = sorted(stat_dict.keys(), key=lambda x: stat_dict[x][1], reverse=True)
    return stat_dict


def export_csv(data_dict):
    # name of csv file
    filename = "country_average.csv"
    filename_2 = "medalists_details.csv"
    fields = ["Country", "Average_medals_overall"]
    fields_2 = ["Medalist", "Country", "Number_of_Medals"]
    rows = []
    rows_2 = []
    stat_dict = generate_report_result_only(data)

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing the fields
        writer.writeheader()

        # writing the data rows
        for key in stat_dict:
            row = {'Country': key, 'Average_medals_overall': stat_dict[key][1]}
            rows.append(row)
        writer.writerows(rows)

        # writing to csv file
    with open(filename_2, 'w') as csvfile:
        # creating a csv writer object
        writer_2 = csv.DictWriter(csvfile, fieldnames=fields_2)

        # writing the fields
        writer_2.writeheader()
        # writing the data rows
        for key in data_dict:
            for values in data_dict[key]:
                temp_row = {"Medalist": values[0], "Country": key, "Number_of_Medals": values[1]}
            rows_2.append(temp_row)
        writer_2.writerows(rows_2)


def import_data_file(line_flag_number=0):
    filename = input("Filename: ")
    file_ins = open(filename, "r+")

    olympian_name = []

    while True:
        line_flag_number = line_flag_number + 1

        temp = file_ins.readline()

        if temp == "":
            break

        olympian, medals = temp.split(";")

        if olympian == '' or medals == '\n':
            print(f"Blank entry on line {line_flag_number}, not added")
            continue
        elif olympian in olympian_name:
            print(f"{olympian} on line {line_flag_number} already entered, not added")
        elif not (0 <= int(medals) <= 35):
            print(f"Incorrect medal number on line {line_flag_number}, not added")
            continue
        else:
            medals = medals.split('\n')[0]
            medals = int(medals)
            data[country].append((olympian, medals))
            olympian_name.append(olympian)

    print(data)


while True:

    if country is not None:
        print("Current Country: ", country)

    print("1: Enter Country")
    print("2: Import Data")
    print("3: Generate Report")
    print("4: Export CSV")
    print("Q: Quit")
    print("--------------------------")
    option = input("Enter Your Choice [1/2/3/4/Q]: ")

    if option in ["Q", "q"]:
        print("Quit")
        break

    if option == "1":
        country = take_country(data)
        continue

    elif option == "2":
        line_flag = 0
        import_data_file(line_flag)
        continue

    elif option == "3":
        _ = generate_report(data)
        continue

    elif option == "4":
        export_csv(data)
