num = int(input("Enter The Value  : "))

# if num==1:
#     print("ONE")
# elif num==2:
#     print("TWO")
# elif num==3:
#     print("THREE")


match num:
    case 1:
        print("ONE")
    case 2:
        print("TWO")
    case 3:
        print("THREE")
    case other:
        print("Not Define")