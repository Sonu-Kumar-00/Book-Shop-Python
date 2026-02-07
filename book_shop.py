class BookShop:
    def __init__(self):
        self.books ={
            "python":{"price":300,"stock":10},
            "java":{"price":250,"stock":8},
            "c++":{"price":200,"stock":5}
        }
            
        
    def display_books(self):
        print("\nAvailable Books:")
        print("-" * 40)
        for name, details in self.books.items():
            print(f"{name} | Price: {details['price']} | Stock: {details['stock']}")
        print("-" * 40)

    def buy_book(self):
        book= input("Enter book name: ").strip().lower()

        if book in self.books:
            qty = int(input("Enter quantity: "))
            
            if qty <= self.books[book]["stock"]:
                total = qty * self.books[book]["price"]
                self.books[book]["stock"] -= qty

                print("\n----- BILL -----")
                print("Book:", book.upper())
                print("Quantity:", qty)
                print("Total Price:", total)
                print("----------------")
            else:
               print(" Not enough stock")
        else:
            print(" Book not found")

    def rent_book(self):
        book = input("Enter book name: ").strip().lower()

        if book in self.books:
            qty = int(input("Enter quantity: "))

            if qty <= self.books[book]["stock"]:
                rent_price = (self.books[book]["price"] * qty) // 4
                self.books[book]["stock"] -= qty
                
                print("\n----- RENT BILL -----")
                print("Book:", book.upper())
                print("Quantity:", qty)
                print("Rent Price:", rent_price)
                print("---------------------")
            else:
                print(" Not enough stock")
        else:
           print(" Book not found")

    def menu(self):
      while True:
       print("""
       \n1. Display Books
        2. Buy Book
        3. Rent Book
        4. Exit
        """)

       choice = input("Enter your choice: ")

       if choice == "1":
        self.display_books()
       elif choice == "2":
        self.buy_book()
       elif choice == "3":
        self.rent_book()
       elif choice == "4":
        print("Thank you for visiting Book Shop ")
        break
       else:
        print(" Invalid choice")

# Run program
shop =BookShop() 
shop.menu() 
    