fileName = open("animal.txt", "w")
fileName.close()

user_input = True
while user_input:
    animal = input("Enter the animal: ")
    owner = input("Enter the animal's owner :")
    name = input("Enter the animal's name: ")

    result_str = [str(animal), str(owner), str(name)]

    with open('animal.txt', 'a') as f:
        f.writelines('\n'.join(result_str))
        fileName.close()

    temp_user_input = input("Do you want to enter another animal?")
    temp_user_input = str(temp_user_input)
    flag = True

    while True:
        temp_user_input = input("Do you want to enter another animal? : ")
        temp_user_input = str(temp_user_input)

        if temp_user_input == "Yes":
            break
        elif temp_user_input == "No":
            exit()
        else:
            print("Please Enter either Yes or No")

