# list for storing input data
data = []

while True:
    name = input("Name: ")
    medals = input("Medals: ")

    data.append((name, medals))

    input_continue = input("Continue? [y/n] ")

    if input_continue == 'n':
        break

# sample separator
print("-----------------------")

for inputs in data:
    print(f"{inputs[0]}\t\t{inputs[1]}")
