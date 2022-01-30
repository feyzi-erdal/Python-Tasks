age = int(input("Are you a cigarette addict older than 75 years old ?"))
chronic = input("Do you have a severe chronic disease ? Please write 'Yes or No'!").capitalize()
immune = input("Is your immune system too weak ? Please write 'Yes or No'!").capitalize()

if age > 75 and chronic == "Yes" and immune == "Yes":
    print("You are in risky group!")
else:
    print("You are NOT in risky group!")