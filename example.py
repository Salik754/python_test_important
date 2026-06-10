"""
Cafeteria Scanner Terminal
Scans items, calculates subtotal, tax, and total.
"""

# ===== CONSTANTS =====
TAX_RATE = 0.12

# ===== MENU (DICTIONARY) =====
menu = {
    "sandwich": 5.50,
    "juice": 2.00,
    "cookies": 1.50,
    "burger": 6.00,
    "fries": 2.50,
    "salad": 4.00,
    "drink": 1.75,
    "pizza": 4.50,
}

# ===== FUNCTIONS =====

def scan_items():
    """Scan items one by one until user types 'exit'."""
    tray = []     # LIST to store items
    
    while True:
        item = input("scan item: ").strip().lower()
        
        if item == "exit":
            break
        
        if item in menu:
            tray.append(item)
            print(f"-> {item} added to tray")
        else:
            print(f"-> {item} not found on menu")
    
    return tray

def calculate_subtotal(tray):
    """Sum up the prices of all items in tray."""
    subtotal = 0
    for item in tray:
        subtotal += menu[item]
    return subtotal

def calculate_tax(subtotal):
    """Calculate tax on subtotal."""
    return subtotal * TAX_RATE

def print_receipt(tray, subtotal, tax, total):
    """Print the final receipt."""
    print("\n---Cafeteria receipt---")
    for item in tray:
        print(f"{item}: ${menu[item]:.2f}")
    print("----------------------")
    print(f"subtotal: ${subtotal:.2f}")
    print(f"tax (12%): ${tax:.2f}")
    print(f"total: ${total:.2f}")
    print("-----------------------")

# ===== MAIN =====

def main():
    """Run the cafeteria scanner."""
    print("welcome to the cafeteria scanner terminal")
    print("Enter items one by one and press exit when tray is full")
    print()
    
    tray = scan_items()
    subtotal = calculate_subtotal(tray)
    tax = calculate_tax(subtotal)
    total = subtotal + tax
    
    print_receipt(tray, subtotal, tax, total)

if __name__ == "__main__":
    main()