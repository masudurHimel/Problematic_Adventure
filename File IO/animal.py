user_input = True
while user_input:
    animal = input("Enter the animal: ")
    owner = input("Enter the animal's owner :")
    name = input("Enter the animal's name: ")

    print(f"Animal: {animal} | Owner: {owner} | Animal's name: {name}")

    while True:
        temp_user_input = input("Do you want to enter another animal? : ")
        temp_user_input = str(temp_user_input)

        if temp_user_input == "Yes":
            break
        elif temp_user_input == "No":
            exit()
        else:
            print("Please Enter either Yes or No")

