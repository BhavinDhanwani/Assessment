#  Fruit Market :

menu="""
    WELCOME TO FRUIT MARKET

    1) Manager
    2) Customer
"""
product={}  # Creating Blank Dictionary

flag=True
while flag:
    print(menu)
    choice=int(input("Select Your Role : "))
    status=True
    if choice==1:
        # Manager panel
        print("""
        FRUIT MARKET MANAGER
        
        1) Add Fruit Stock
        2) View Fruit Stock
        3) Update Fruit Stock
""")
        choice=int(input("Enter Your Choice : "))
        if choice==1:
            while status:
                print("ADD FRUIT STOCK")
                specific_product={}
                product_name=input("Enter Fruit Name : ")
                product_qty=int(input("Enter Qty (in kg): "))
                product_price=int(input("Enter product price of 1kg qty : "))

                if product_name in product:
                    # fetch old qty from the dictionary.
                    old_qty=product[product_name]['qty']
                    specific_product['qty']=old_qty+product_qty
                    specific_product['price']=product_price
                else:
                    specific_product["qty"]=product_qty
                    specific_product["price"]=product_price

                product[product_name]=specific_product

                print("Product Added = ",product)

                choice = input("Do you want to add more product : ").lower()
                if choice=='y' or choice=='yes':
                    status=True
                else: 
                    status=False
                    print("~"*50)
                    choice = input("Do you want to perform more operations : ").lower()
                    if choice=='y' or choice=='yes':
                        flag=True
                    else: 
                        flag=False
        elif choice==2:
            print("Available Fruit Stock",product)
        elif choice==3:
            print("Update Fruit Stock")
            specific_product
    elif choice==2:
        # customer panel
        print("\n ::::::: PRODUCT MENU ::::::: ")
        for k in product:
            print(f"{k} - 1kg price is RS. {product[k]['price']}")
        status=True
        cart={}
        while status:
            prd=input("What do you want to buy? : ")
            if prd in product:
                prd=cart
                print(cart)
            else:
                print(f"{prd} is not available.")
                qty=int(input("Enter quantity : "))
                if qty in product_qty:
                    print("Stock out")
                choice=input("Do you want something else? ").lower()
                if choice=='y' or choice=='yes':
                    status=True
                else:
                    status=False
    else:
        print("Invalid Input enter 1 or 2 only.")