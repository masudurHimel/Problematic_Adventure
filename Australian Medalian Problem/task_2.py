# list for storing input data
data = []
sum_result = 0

while True:
    name = input("Name: ")
    medals = input("Medals: ")

    # validation check
    if name and medals and 0 <= int(medals) <= 35:
        data.append((name, medals))
    else:
        if not medals or not name:
            print("Blank Entry")
        elif not 0 <= int(medals) <= 35:
            print("Incorrect Medal Entry")

    while True:
        input_continue = input("Continue? [y/n] ")
        if input_continue not in ['Y', 'y', 'N', 'n']:
            continue
        else:
            break
    if input_continue in ['n', 'N']:
        break

# sample separator
print("Results")
print("-----------------------")

for inputs in data:
    print(f"{inputs[0]} \t {inputs[1]}")
    sum_result = sum_result + int(inputs[1])

print("-----------------------")
average_medals = "{:.2f}".format(sum_result/len(data))
print(f"Average Medals \t {average_medals}")
