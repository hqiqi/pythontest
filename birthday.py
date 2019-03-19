import datetime
now = datetime.datetime.now()

invalid_input = True


def start():
    try:
        birth_year = int(input("Enter your birthday year "))
    except ValueError:
        raise ValueError("Wrong Input, try again")
        continue
    else:
        if birth_year >= now.year:
            raise ValueError
        else:
            age = now.year - birth_year
            print("You are " + str(age) + ' years old')
            invalid_input = False
            exit()


while invalid_input == True:
    start()
