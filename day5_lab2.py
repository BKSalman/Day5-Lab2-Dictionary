dict = {
"Amal" : 1111111111,
"Mohammed" : 2222222222, 
"Khadijah" : 3333333333 , 
"Abdullah" : 4444444444 , 
"Rawan" : 5555555555 , 
"Faisal" : 6666666666 ,
"Layla" : 7777777777
}

def get_key(dict, value):
    owner = [k for k, v in dict.items() if v == value]
    if (not owner):
        print("Sorry, the number is not found")
        return
    print(owner[0])

number = input("Enter the phone number\n")

if number.isdigit() and len(number) == 10:
    get_key(dict, int(number))
else:
    print("This is invalid number")
