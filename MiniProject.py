import mysql.connector
import re


connector = mysql.connector.connect(
    host='localhost',
    database='miniproject',
    user='root',
    password=''
)
cc=connector.cursor()

print("Welcome the the product Shop!\n")

while True:
    print("===== Login Page =====")
    print("1. Admin Login")
    print("2. User Login")
    print("3. Exit")

    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("You've successfully logged in as Admin!")

        while True:
            while True:
                print("===== Main Menu =====")
                print("1. Insert Product")
                print("2. View all Products")
                print("3. Remove Product")
                print("4. View Order Records")  # New Option
                print("5. Return to Login Page")

                admin_choice = int(input("Enter your choice: "))

                if admin_choice == 1:
                    product_id = input("Enter Product ID: ")
                    product_name = input("Enter Product Name: ")
                    product_price = input("Enter Product Price: ")
                    product_amt = int(input("Enter Product Quantity: "))

                    query = "INSERT INTO admin (product_id, product_name, product_price, product_amt) VALUES (%s, %s, %s, %s)"
                    values = (product_id, product_name, product_price, product_amt)
                    cc.execute(query, values)
                    connector.commit()
                    print("Product inserted successfully!")

                elif admin_choice == 2:
                    query = 'SELECT * FROM `admin`'
                    cc.execute(query)
                    results = cc.fetchall()
                    for x in results:
                        print(x)

                elif admin_choice == 3:
                    product_id = int(input("Enter Product ID to remove: "))
                    query = "DELETE FROM admin WHERE product_id = %s"
                    cc.execute(query, (product_id,))
                    connector.commit()
                    print("Product removed successfully!")

                elif admin_choice == 4:  # New functionality
                    query = "SELECT o.order_id, o.order_name, o.order_price, a.product_name, a.product_price FROM order_table o JOIN admin a ON o.order_name = a.product_name"

                    cc.execute(query)
                    results = cc.fetchall()
                    if results:
                        print("\n--- Order Records ---")
                        for row in results:
                            print(
                                f"Order ID: {row[0]}, Order Name: {row[1]}, Order Price: ₹{row[2]:.2f}, Product Name: {row[3]}, Product Price: ₹{row[4]:.2f}")
                    else:
                        print("No orders have been made yet.")

                elif admin_choice == 5:
                    break

                else:
                    print("Invalid choice. Please try again.")


    elif choice == 2:
        print("You've successfully logged in as User!")

        while True:
            print("===== Main Menu =====")
            print("1. User Registration")
            print("2. View All Products")
            print("3. Search for a Product")
            print("4. Buy a Product")
            print("5. Back to Main Menu")

            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:

                while True:
                    user_name = input("Enter your Name: ")
                    if user_name.strip():
                        break
                    print("Name cannot be empty. Please enter a valid name.")

                while True:
                    user_password = input("Enter your Password: ")
                    if len(user_password) >= 8:
                        break
                    print("Password must be at least 8 characters long and include both letters and numbers.")

                while True:
                    user_email = input("Enter your Email: ")
                    if re.match(r"[^@]+@[^@]+\.[^@]+", user_email):
                        break
                    print("Please enter a valid email address.")

                while True:
                    user_contact = input("Enter your Contact number: ")
                    if len(user_contact) == 10 and user_contact.isdigit():
                        break
                    print("Contact number must be exactly 10 digits.")

                values = (user_name, user_password, user_email, user_contact)
                insert_query = "INSERT INTO user (user_name,user_password,user_email,user_contact) values(%s,%s,%s,%s)"
                cc.execute(insert_query, values)
                connector.commit()

            if user_choice == 2:
                cc.execute("SELECT * FROM admin")
                results = cc.fetchall()
                print("\n--- Available Products ---")
                for row in results:
                    print(f"product_id: {row[0]}, product_name: {row[1]},product_price: {row[2]}, product_amt: {row[3]}")

            elif user_choice == 3:
                product_name = input("Enter Product Name to search: ")
                query = "SELECT * FROM admin WHERE product_name LIKE %s"
                cc.execute(query, (f"%{product_name}%",))
                results = cc.fetchall()
                if results:
                    print("\n--- Search Results ---")
                    for row in results:
                        print(f"product_id: {row[0]}, product_name: {row[1]},product_price: {row[2]}, product_amt: {row[3]}")
                else:
                    print("No products found with this name.")

            elif user_choice == 4:
                product_id = int(input("Enter the ID of the product you want to buy: "))
                quantity = int(input("Enter the quantity you want to buy: "))

                # Fetch car details from the admin table
                query = "SELECT * FROM admin WHERE product_id = %s"
                cc.execute(query, (product_id,))
                product = cc.fetchone()

                if product:
                    product_id, product_name, product_price, product_amt = product[0], product[1], product[2], product[3]
                    product_amt = int(product_amt)

                    if product_amt >= quantity:
                        total_price = product_price * quantity

                        order_name = input("Enter your Order name for the order: ")
                        order_price = total_price
                        order_id = input("Enter separate Order ID")

                        query = "INSERT INTO `order_table` (order_id, order_name, order_price) VALUES (%s, %s, %s)"
                        values = (order_id, order_name, order_price)
                        cc.execute(query, values)
                        connector.commit()

                        print(f"\n--- Purchase Confirmation ---")
                        print(f"Product Name: {product_name}")
                        print(f"ID: {product_id}")
                        print(f"Quantity: {quantity}")
                        print(f"Total Price: ₹{total_price:.2f}")
                        print("Your purchase has been recorded in the order table. Thank you!")
                    else:
                        print(f"Sorry, only {product_amt} units of {product_name} are available in stock.")
                else:
                    print("Product not found.")

            elif user_choice == 5:
                break

            else:
                print("Incorrect choice! PLease enter the correct choice...")

    elif choice == 3:
        print("Thankyou for accessing the software!")
        break

    else:
        print("Invalid choice. Please try again.")