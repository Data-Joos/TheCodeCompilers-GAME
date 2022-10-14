
success = False


while not success:
    print("Skriv din ålder: ")
    inmatning = input()

    try:
        ålder = int(inmatning)
        print("Din ålder är ", ålder)
        success = True

    except ValueError as err:
        print(err)  
print("Här är slutet på programmet.")