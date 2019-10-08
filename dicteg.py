Phone = input("phone:")
phone = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero"
}
new_number =  " "
for ch in phone:
    new_number += phone.get(ch ,"!") + " "
print(new_number)

