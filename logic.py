available={"1.1.1.1", "2.2.2.2", "3.3.3.3"}
unavailable = set()
user_input = ""

while user_input!="exit":
    # Get input from the user and store it in a variable
    user_input = input("Enter something: ")

    if user_input == "":
        continue

    # Print the input
    print("You entered:", user_input)

    x = user_input.split()

    if x[0].upper()=="ASK" and len(available) > 0:
        offered = available.pop()
        print("Offer "+offered)
        unavailable.add(offered)

    if (len(x) > 1 and x[0].upper()=="RENEW" and x[1] in unavailable):
        print("RENEWED for "+x[1])

    if (len(x) > 1 and x[0].upper()=="RELEASE" and x[1] in unavailable):
        print("RELEASED for "+x[1])
        unavailable.remove(x[1])
        available.add(x[1])

    if (len(x) > 1 and x[0].upper()=="STATUS"):
        if x[1] in available:
            print(x[1]+" AVAILABLE")
        elif x[1] in unavailable:
            print(x[1]+" ASSIGNED")
        else:
            print("Invalid.")