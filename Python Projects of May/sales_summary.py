# this function gets the sales data from the user
# it also takes the name of the item, price, and quantity sold
def get_sales():
    sales={}
    try:
        total_items=int(input("How many different items do you want to enter?"))            # Get the number of items
    except ValueError: 
        print("Please enter a valid number.")
        return sales()

    for _ in range(total_items):
        sales_item = input("Enter the name of the item: ")                                  # Get the name of the item
        if not sales_item:
            print("Item name cannot be empty.")
            continue
        try:
            item_price = float(input(f"Enter the price of {sales_item}: Tk "))              # Get the price of the item  
            item_quantity = int(input(f"Enter the quantity of {sales_item}: Pieces "))      # Get the quantity of the item
        except ValueError:
            print("Please enter valid numbers for price and quantity.")
            continue

        if item_quantity>0 and item_price>0:
            if sales_item in sales:                 
                sales[sales_item]['item_quantity'] += item_quantity
                sales[sales_item]['revenue'] += item_price * item_quantity
                
            else:
                sales[sales_item]={'item_quantity': item_quantity, 'revenue': item_price * item_quantity}
        else:
            print("Please input positive numbers for price and quantity.")
    return sales
# this function generates a summary of the sales data
# also prints the item name, quantity sold, and revenue made for every item
def generate_sales_summary(sales):
    print("_____Sales Summary_____")
    print("Item Name-----Number of Items-----Revenue")
    total_revenue = 0
    for item, data in sales.items():
        print(f"{item}---{data['item_quantity']}---{data['revenue']}")
        total_revenue += data['revenue']
    print(f"Total Revenue: {total_revenue:.2f} Tk")

def main():
    sales = get_sales()
    if sales:
        generate_sales_summary(sales)
if __name__ == "__main__":
    main()