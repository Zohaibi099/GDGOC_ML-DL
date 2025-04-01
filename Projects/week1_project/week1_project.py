# import re
# def validate_email(email):
#     print("Check if the email contains '@' and '.' and follows a valid format.")
#     pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
#     return re.match(pattern, email)

# userinfo = {}
    
# userinfo['name'] = input("Enter your name: ")
# userinfo['age'] = input("Enter your age: ")
    
# while True:
#         email = input("Enter your email: ")
#         if validate_email(email):
#             userinfo['email'] = email
#             break
#         else:
#             print("Invalid email format. Please enter a valid email.")
    
# userinfo['favorite_number'] = input("Enter your favorite number: ")
    
# print("\nUser Information:")
# print("Name: {userinfo['name']}")
# print("Age: {userinfo['age']}")
# print("Email: {userinfo['email']}")
# print("Favorite Number: {userinfo['favorite_number']}")

# def is_evan(num):
#      if(num%2==0):
#           print(num," is an even number")
#      else:
#           print(num," is an odd number")

# number= int(input("enter a number to check even or odd: "))
# is_evan(number)

# def temperature_converter():
#     while (True):
#         temp=int(input("enter the temperature you want to convert: "))
#         scale=input("press c or C for Celcius | f or F for Farenheit: ")
#         if scale == 'C'or scale =='c':
#             print("Converted Tempeature: ", (temp * 9/5) + 32)
#             break
#         elif scale =='F'or scale =='f':
#             print("Converted Tempeature: ",  (temp - 32) * 5/9)
#             break
#         else:
#             print("Invalid scale. Use 'C' for Celsius or 'F' for Fahrenheit.")

# temperature_converter()



# def max_min():
#     array = []
#     print("Enter 5 Numbers:")
#     for i in range(5):
#         array.append(int(input()))  

#     max_value = max(array)  
#     min_value = min(array)  
#     print("Maximum Value:", max_value)
#     print("Minimum Value: ",min_value)
# max_min()


# def student_details():
#     list = []  
#     for i in range(3):
#         print("\nEnter details for Student: ",{i+1})
#         name = input("Name: ")
#         age = int(input("Age: "))
#         grade = input("Grade: ")
#         list.append((name, age, grade))  
#     students= dict((name, (age, grade)) for name, age, grade in list)
#     print("\nStudent Dictionary:")
#     print(students)

# student_details()


def update_inventory(inventory_dict, item, quantity):
    if item in inventory_dict:
        inventory_dict[item] = max(0, inventory_dict[item] + quantity) 
    else:
        print("Item '{item}' not found in inventory.")
    return inventory_dict
inventory = {
    "Apples": 10,
    "Bananas": 5,
    "Oranges": 8,
    "Grapes": 12,
    "Mangoes": 7
}
print("Current Inventory:", inventory)

for i in range(3):
    item = input("\nEnter item to update: ")
    quantity = int(input("Enter quantity to add/remove (use negative for removal): "))
    inventory = update_inventory(inventory, item, quantity)
    print("Updated Inventory:", inventory)
print("\nFinal Inventory:", inventory)
