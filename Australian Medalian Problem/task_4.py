import csv

data = {}
country = None
olympian_name = []


# main menu
def take_country(data_dict):
    country_input = input("Country: ")
    temp = data_dict.get(country_input, None)
    if temp is None:
        data_dict[country_input] = []
    return country_input


def top_five_generator():
    top_five_dict = {}

    for key in data:
        temp_list = data[key]
        temp_sorted_list = sorted(temp_list, key = lambda x: x[1], reverse = True)
        if len(temp_sorted_list) >=5:
            top_five_dict[key] = temp_sorted_list[0:5]
        else:
            top_five_dict[key] = temp_sorted_list[0:len(temp_sorted_list)]
        
    return top_five_dict


def generate_report(data_dict):
    top_average = {}
    print("Results\n")
    print("-----------------------------")
    print("Top 5 Olympic Medalists per Country")
    print("-----------------------------")
    top_five = top_five_generator()

    for key in top_five:
        print(f"Country = {key}")
        temp_average = 0
        for value in top_five[key]:
            print(f"{value[0]} {value[1]}")
            temp_average = temp_average + int(value[1])

        temp_average = "{:.2f}".format(temp_average / 5)
        top_average[key] = temp_average

        if len(top_five[key]) < 5: 
            print("Note less than 5 athletes listed")

        print("-----------------------------")
    
    print("Country Results")
    for key in top_average:
        print(f"{key} {top_average[key]}")
    print("-----------------------------")


def generate_report_result_only(data_dict):
    top_average = {}
    top_five = top_five_generator()

    for key in top_five:
        temp_average = 0
        for value in top_five[key]:
            temp_average = temp_average + int(value[1])

        temp_average = "{:.2f}".format(temp_average / 5)
        top_average[key] = temp_average
    return top_five, top_average

def export_csv(data_dict):
    # name of csv file
    filename = "countryTask4.csv"
    filename_2 = "olympianTask4.csv"
    fields = ["Country", "Average"]
    fields_2 = ["Olympians", "Country", "Medal tally"]
    rows = []
    rows_2 = []
    top_five, top_average = generate_report_result_only(data)

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing the fields
        writer.writeheader()

        # writing the data rows
        for key in top_average:
            row = {'Country': key, 'Average': top_average[key]}
            rows.append(row)
        writer.writerows(rows)

        # writing to csv file
    with open(filename_2, 'w') as csvfile:
        # creating a csv writer object
        writer_2 = csv.DictWriter(csvfile, fieldnames=fields_2)

        # writing the fields
        writer_2.writeheader()
        # writing the data rows
        for key in top_five:
            for values in top_five[key]:
                temp_row = {"Olympians": values[0], "Country": key, "Medal tally": values[1]}
                rows_2.append(temp_row)
        writer_2.writerows(rows_2)


def import_data_file(line_flag_number=0):
    filename = input("Filename: ")
    file_ins = open(filename, "r+")

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
        generate_report(data)
        continue

    elif option == "4":
        export_csv(data)
