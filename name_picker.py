from random import randint

print("\nWelcome to the Random Name generator by Thijz!")

input("Press a key to continue......")

name_amount = int(input("\nInput how many names u want to use: "))
names = []
for x in range(name_amount):
    k = input("Enter name : \n")
    names.append(k)

random_number = randint(0, len(names))

name_number = (random_number - 1)

random_name = names[name_number]
print("\nThe number of the name is : " + str(name_number) + "!!")
print("\nThe name that has been randomly selected is: " + random_name + "!!" + " Congrats!")

input("Press a key to continue......")