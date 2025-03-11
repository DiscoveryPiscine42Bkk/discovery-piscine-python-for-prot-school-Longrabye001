while True:
    user_input = input("What you gotta say? : ")
    print("I got that! Anything else? :", end=" ")

    if user_input.upper() == "STOP":
        break
    else:
        print(user_input)
