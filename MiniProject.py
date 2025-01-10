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
        xyz=int(input("Enter password:"))
        if xyz == 444:
            print("You've successfully logged in as Admin!")

            while True:
                print("===== Main Menu =====")
                print("1. Insert Product")
                print("2. View all Products")
                print("3. Remove Product")
                print("4. View Order Records")
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

                elif admin_choice == 4:
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
        else:
            print("Incorrect password! Admin login unsuccessful!")

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

                print("1. Sign up as User")
                print("2. Sign in as User")
                reg_choice = int(input("Enter your choice:"))
                if reg_choice == 1:
                    while True:
                        user_contact = input("Enter your Contact number: ")
                        if len(user_contact) == 10 and user_contact.isdigit():
                            break
                        print("Contact number must be exactly 10 digits.")

                    while True:
                        user_name = input("Enter your name:")
                        if user_name.strip():
                            break
                        print("Name cannot be empty. Please enter a valid name.")

                    while True:
                        user_password = input("PLease enter the password:")
                        if len(user_password) >= 8:
                            break
                        print("Password must consist minimum 8 characters")

                    while True:
                        user_email= input("Enter your Email: ")
                        if re.match(r"[^@]+@[^@]+\.[^@]+", user_email):
                            break
                        print("Please enter a valid email address.")

                    user_question = input("Enter a security question (e.g., What is your mother's maiden name?): ")
                    user_answer = input("Enter the answer to your security question: ")

                    query_email = "SELECT * FROM user WHERE user_email = %s"
                    cc.execute(query_email, (user_email,))
                    user_info = cc.fetchone()

                    if user_info:
                        print("This email is already registered. Please log in.")
                    else:
                        values = (
                        user_contact, user_name, user_password, user_email, user_question, user_answer)
                        insert_query = "INSERT INTO user(user_contact, user_name, user_password, user_email, user_question, user_answer) VALUES (%s, %s, %s, %s, %s, %s)"
                        cc.execute(insert_query, values)
                        connector.commit()
                        print("Registration successful! You can now log in.")

                elif reg_choice == 2:
                    user_email = input("Enter your Email: ")
                    user_password = input("Enter your Password: ")

                    query = "SELECT * FROM user WHERE user_email = %s AND user_password = %s"
                    cc.execute(query, (user_email, user_password))
                    user_info = cc.fetchone()

                    if user_info:
                        print(f"Welcome back..! You are successfully logged in.")
                    else:
                        print("Invalid email or password. Please try again or sign up.")

                        reset_choice = input("Forgot Password? (yes/no): ").strip().lower()
                        if reset_choice == "yes":
                            query = "SELECT user_question, user_answer FROM user WHERE user_email = %s"
                            cc.execute(query, (user_email,))
                            result = cc.fetchone()

                            if result:
                                user_question, correct_answer = result
                                print(f"Security Question: {user_question}")
                                user_answer = input("Answer: ")

                                if user_answer.lower() == correct_answer.lower():
                                    while True:
                                        New_password = input("Enter your new password: ")
                                        if len(New_password) >= 8:
                                            break
                                        print("Password must be at least 8 characters long.")

                                    query = "UPDATE `user` SET user_password = %s WHERE user_email = %s"
                                    # query1 = "UPDATE `order` SET user_password=%s WHERE user_email=%s"
                                    cc.execute(query, (New_password, user_email))
                                    # cc.execute(query1, (New_password, user_email))
                                    connector.commit()
                                    print("Your password has been successfully reset!")
                                else:
                                    print("Incorrect answer. Please try again.")
                            else:
                                print("No account found with that email. Please register.")

            if user_choice == 2:
                cc.execute("SELECT * FROM admin")
                results = cc.fetchall()
                print("\n--- Available Products ---")
                for row in results:
                    print(
                        f"product_id: {row[0]}, product_name: {row[1]},product_price: {row[2]}, product_amt: {row[3]}")

            elif user_choice == 3:
                product_name = input("Enter Product Name to search: ")
                query = "SELECT * FROM admin WHERE product_name LIKE %s"
                cc.execute(query, (f"%{product_name}%",))
                results = cc.fetchall()
                if results:
                    print("\n--- Search Results ---")
                    for row in results:
                        print(
                            f"product_id: {row[0]}, product_name: {row[1]},product_price: {row[2]}, product_amt: {row[3]}")
                else:
                    print("No products found with this name.")

            elif user_choice == 4:
                product_id = int(input("Enter the ID of the product you want to buy: "))
                quantity = int(input("Enter the quantity you want to buy: "))

                query = "SELECT * FROM admin WHERE product_id = %s"
                cc.execute(query, (product_id,))
                product = cc.fetchone()

                if product:
                    product_id, product_name, product_price, product_amt = product
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

    elif choice == 3:
        print("Thank you for accessing the software!")
        break

    else:
        print("Invalid choice. Please try again.")
