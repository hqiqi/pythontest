
check = False

while check == False:
    number_input = int(input("Integer: "))
    if number_input == 0:
        print("bye")
        check = False
        break
    elif number_input>20 and number_input<200:
        print(str(number_input)+" passes the test!")
        check = False
        break
    else:
        print(str(number_input)+" fails the test.")
