Record = set()

print("------------ Registration Form ------------")

while True:
    print("\n------------ Main Menu ------------")
    print("1. Register")
    print("2. Record")
    print("3. Exit Program")

    choice = int(input("Enter Choice: "))
    if choice in range(1, 4):
        if choice == 1:
            print("Registration")
            name = input("Enter Full Name:").strip()

            while True:
                mobile = input("Enter a 10-digit Mobile No.: ").strip()
                if len(mobile) == 10 and mobile.isdigit():
                    break
                print("Invalid input! Enter a 10-digit Mobile No.")

            while True:
                password = input("Enter a 6-14 digit password:")
                if 6 <= len(password) <= 14:
                    break
                print("Invalid input! Enter a 6-14 digit password.")

            entry=(name, mobile, password)
            Record.add(entry)
            print(f"Registration successful for {name}")

        elif choice == 2:
            print("------------ Record ------------")
            if Record:
                for idx, rec in enumerate(Record, start=1):
                    print(f"{idx}. Name: {rec[0]}, Mobile: {rec[1]}")
            else:
                print("No records found.")

        elif choice == 3:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! PLease select a valid choice.")

