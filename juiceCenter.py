# #  Menu list
# menu = {
#  'Veg Sandwich':80,  
#  'Cheese Grilled Sandwich':120, 
#  'Masala Omelette with Toast':100, 
#  'Pancakes with Honey':150,  
#  'French Fries':90,  
#  'Cheese Garlic Bread':110,  
#  'Veggie Momos (6 pcs)':100,  
#  'Chicken Momos (6 pcs)':130, 
# }

# # Greetings
# print("Wlecome to PYTHON Restraurant")
# print("Veg Sandwich:80,\nCheese Grilled Sandwich:120,\nMasala Omelette with Toast:100,\nPancakes with Honey:150,\nFrench Fries:90,\nCheese Garlic Bread:110,\nVeggie Momos (6 pcs):100,\nChicken Momos (6 pcs):130")

# Total_order = 0
# # Order taking

# item1 = input("Enter the food which you want to order:")
# if item1 in menu:
#     Total_order += menu[item1]
#     print(f"Your order {item1}Succesfully Placed!")
# else: 
#     input(f"Ordered item {item1} is not available yet!!")

# another_item = input("Do you want to like something else to order(Y/N)")
# if another_item == 'Y':
#     item2 = input("Enter the food name here:")
#     if item2 in menu :
#       Total_order += menu[item2]
#       print(f"Your order {item2} succesfuuly placed!")
#     else:
#          input(f"Ordered item {item2} is not available yet!!")

# Menu list
menu = {
    'Orange Juice': 90,
    'Apple Juice': 100,
    'Mango Juice': 110,
    'Pineapple Juice': 120,
    'Watermelon Juice': 80,
    'Grape Juice': 95,
    'Lemonade': 85,
    'Pomegranate Juice': 130
}

# Greeting
print("\n 🍽️ Welcome to PYTHON Restaurant! 🍽️")
print("\nHere's our menu:\n")
print("------------------------------------------------")
for index, (item, price) in enumerate(menu.items(), 1):
    print(f"{index}. {item} - ₹{price}")
print("------------------------------------------------")

# Order processing
total_order = 0
order_list = []

while True:
    try:
        choice = input("\nEnter the menu number or food item to order (or type 'done' to finish): ").strip()
        if choice.lower() == 'done':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(menu):
            item = list(menu.keys())[int(choice) - 1]
        elif choice in menu:
            item = choice
        else:
            print("❌ Invalid choice. Please select a valid menu item.")
            continue
        
        total_order += menu[item]
        order_list.append(item)
        print(f"✅ {item} added to your order!")
    except Exception as e:
        print("❌ An error occurred. Please try again.")

# Display final order summary
if order_list:
    print("\n📝 Your final order:")
    for ordered_item in order_list:
        print(f"- {ordered_item}: ₹{menu[ordered_item]}")
    print(f"💸Total Bill: ₹{total_order}")
else:
    print("You did not order anything.")

print("\n🙏 Thank you for visiting PYTHON Restaurant! Have a great day! 😊")