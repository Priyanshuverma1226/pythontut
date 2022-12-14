import random

random_number=random.randint(1,20)

i=1
while i<=8:
    user_value=int(input("Enter The Number : "))
    if random_number==user_value:
        print(f"You Won Game You will Take {i}")

        break
    elif user_value<random_number:
        print("Pls Enter the Large number")
    elif user_value>random_number:
        print("Pls Enter the Small value")

    i=i+1
    
if i>8:
    print("Game IS Over")