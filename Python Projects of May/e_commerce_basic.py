#this function is for adding items

def add_item(cart):
    try:
        name= input("Enter item name:")
        quantity=int(input("Enter quantity: "))
        price= int(input("Enter price for per item: "))

        if quantity <= 0 or price <=0:
            print("Quantity and Price must be given in positive numbers")
            return
        
        cart.append({"name":name, "quantity":quantity,"price":price})
    except ValueError:
        print("Not valid input! Please enter valid input.")
#this function is for viewing cart

def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return
    print("Cart items:-")
    for idx,item in enumerate(cart,start=1):
        unit_text = "unit" if item["quantity"] == 1 else "units"
        print(f"{idx}.{item['quantity']} {unit_text} of {item['name']} at {item['price']:.2f} Tk per item.")
#this function is for calculating total price and discount

def calculate_total(cart):
    total=sum(item["quantity"]* item["price"] for item in cart)
    discount= 0
    if total> 1000:
        discount = 0.25*total
        total -= discount
    return total,discount
#this function is for checking out

def checkout(cart):
    if not cart:
        print("Nothing to checkout. Your cart is blank")
        return
    view_cart(cart)
    total,discount= calculate_total(cart)
    print(f"Subtotal:{total+discount:.2f} TK")

    if discount>0:
        print(f"Discount applied: {discount} @ 0.25%")
    print(f"Total to pay: {total:.2f} TK")

    cart.clear()
    print("Cart has been cleared after each checkout")

#this function is for the user to choose their service accordingly

def show_menu():
    print("Welcome to Shopping cart menu. Your cart will be cleard automatically after checking out.")
    print("1. add item")            
    print("2. view cart")            
    print("3. checkout")            
    print("4. exit")
    
#this function is for managing all those mentioned functios sequently 

def main():
    cart=[]
    while True:
        show_menu()
        choice=input("Select from 1 to 4:")
        if choice=="1":
            add_item(cart)
        elif choice =="2":
            view_cart(cart)
        elif choice=="3":
            checkout(cart)
        elif choice=="4":
            print("Exit.Thanks for staying with us")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 4")
if __name__ =="__main__":
    main()                        