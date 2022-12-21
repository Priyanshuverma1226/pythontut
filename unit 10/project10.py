

while True:
    c=int(input("Please fill the choice\n Press 1 for add \nPress 2 for Sub\nPress 3 for Multiplication\nPress 4 for Divide"))
    num1=int(input("ENter The Num 1"))
    num2=int(input("ENter The Num 2"))

    match c:
        case 1:
            b=f"{num1}+{num2}"
            print(eval(b))
        case 2:
            b=f"{num1}-{num2}"
            print(eval(b))
        case 3:
            b=f"{num1}*{num2}"
            print(eval(b))
        case 4:
            b=f"{num1}/{num2}"
            print(eval(b))

        