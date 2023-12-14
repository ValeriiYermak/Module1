initial_pin = "1234"
user_pin = input("Enter your pin:")

n = 0

while n < 3: 

    if len(user_pin) == 4 or len(user_pin) == 6:
        if initial_pin == user_pin:
            print("Here your money")
            break
        else:
            print("Sorry, wrong pin. Try again please!")
    else:
        print("Pin should be 4 or 6 digitals.")

    n += 1

print("Good bye!")