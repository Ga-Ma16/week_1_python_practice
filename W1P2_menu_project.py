def display_menu(menu):
    print("\n--- ☕ WELCOME TO THE BLUEPRINT CAFE ☕ ---")
    print(f"{'Item':<20}{'Price':>10}")
    print("-" * 32)
    for item, price in menu.items():
        print(f"{item.capitalize():<20}Rs.{price:>7.2f}")
    print("-" * 32)

def generate_bill(cart, menu):
    print("\n" + "="*35)
    print("         RECEIPT SUMMARY         ")
    print("="*35)
    total = 0
    for item, quantity in cart.items():
        price = menu[item] * quantity
        total += price
        print(f"{item.capitalize():<18} x{quantity:<3} Rs.{price:>8.2f}")
    print("-" * 35)
    print(f"{'TOTAL AMOUNT:':<23} Rs.{total:>8.2f}")
    print("="*35)
    print("   Thank you for dining with us!   \n")

# Using a Dictionary for data mapping
cafe_menu = {
    "espresso": 120.00,
    "latte": 150.00,
    "cappuccino": 160.00,
    "sandwich": 180.00,
    "brownie": 140.00
}

order_cart = {}

# Interactive Menu Loop
while True:
    display_menu(cafe_menu)
    choice = input("Enter the item you want to order (or type 'checkout' to finish): ").strip().lower()
    
    if choice == 'checkout':
        if not order_cart:
            print("Your cart is empty! Add something before checking out.")
            continue
        break
        
    if choice in cafe_menu:
        try:
            qty = int(input(f"How many portions of {choice} would you like? "))
            if qty <= 0:
                print("Quantity must be greater than 0.")
                continue
                
            order_cart[choice] = order_cart.get(choice, 0) + qty
            print(f"✅ Added {qty}x {choice} to your cart.")
        except ValueError:
            print("❌ Invalid quantity. Please enter a whole number.")
    else:
        print("❌ That item isn't on the menu. Please check the spelling.")

generate_bill(order_cart, cafe_menu)