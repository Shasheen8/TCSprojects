Weight = int(input("Weight:"))
Unit = input("(L)bs or (K)gs:")

if Unit.upper() == "L":
    new_weight = Weight * 0.5
    print(f"You are now {new_weight} kgs")
else:
    new_weight= Weight / 0.5
    print(f"You are now {new_weight} lbs")


