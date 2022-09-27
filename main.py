#input-user
def menuUser():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit!")

    UserPick = int(input("Enter a number: "))
    return UserPick


#C
def convertToCelsius(f):
    return int((f - 32) / 1.8)


#F
def convertToFarenheit(c):
    return int(c * 1.8 + 32)


#backend
def mainMenu():
    choice = menuUser()
    while choice != 3:
        if choice == 1:
            #convert C to F
            c = eval(input("Enter a degrees Celsius: "))
            print(str(c) + "C = " + str(convertToFarenheit(c)) + "F")
        elif choice == 2:
            #convert F to C
            f = eval(input("Enter degrees Farenheit: "))
            print(str(f) + "F = " + str(toCelsius(f)) + "C")

        else:
            print("i n v a l i d  e n t r y")
        choice = menu()
