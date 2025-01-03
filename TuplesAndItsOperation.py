while(True):
    print("1.Creating Tuple")
    print("2.Count Particular element form tuple")
    print("3.Show Index of particular element")
    print("4.Insert element at any position")
    print("5.Concatanation of teo tuples are:")
    print("6.Slicing in tuple")
    print("7.Length of Tuple")
    print("8.Exit")

    operation = int(input("Enter your choice: "))


    if operation in range(1,8):

        if operation==1:
            Names1 = tuple(input("\nEnter the elements separated by space in tuple 1: ").split())
            print("The First tuple is:", Names1)

            Names2 = tuple(input("\nEnter the elements separated by space in tuple 2: ").split())
            print("The Second tuple is:", Names2)

        elif operation==2:
            tuple_choice=int(input("\nChoose which tuple to count in (1 or 2): "))
            element = input("\nEnter the element to count: ")

            if tuple_choice == 1:
                if element in Names1:
                    count = Names1.count(element)
                    print(f"The element '{element}' appears {count} times in tuple 1.")
                else:
                    print("Element is not in tuple")

            elif tuple_choice == 2:
                if element in Names2:
                    count = Names2.count(element)
                    print(f"The element '{element}' appears {count} times in tuple 2.")
                else:
                     print("Invalid tuple choice.")

        elif operation==3:
            tuple_choice = int(input("\nChoose which tuple to search in (1 or 2): "))
            element = input("\nEnter the element to find its index: ")

            if tuple_choice == 1:
                if element in Names1:
                    index = Names1.index(element)
                    print(f"The index of '{element}' in tuple 1 is: {index}")
                else:
                    print(f"'{element}' is not in tuple 1.")
            elif tuple_choice == 2:
                if element in Names2:
                    index = Names2.index(element)
                    print(f"The index of '{element}' in tuple 2 is: {index}")
                else:
                    print(f"'{element}' is not in tuple 2.")
            else:
                print("Invalid tuple choice.")

        elif operation==4:
            tuple_choice = int(input("\nChoose which tuple to insert in (1 or 2): "))
            element = input("\nEnter the element to insert: ")
            position = int(input("\nEnter the position to insert the element: "))

            if tuple_choice == 1:
                # Convert tuple to list
                Names1 = list(Names1)
                Names1.insert(position, element)
                # Convert back to tuple
                Names1 = tuple(Names1)
                print("Updated tuple 1:", Names1)
            elif tuple_choice == 2:
                Names2 = list(Names2)
                Names2.insert(position, element)
                Names2 = tuple(Names2)
                print("Updated tuple 2:", Names2)
            else:
                print("Invalid tuple choice.")

        elif operation==5:
            Result=Names1 + Names2
            print("Concatanation of two tuple is:",Result)

        elif operation==6:
            tuple_choice = int(input("\nChoose which tuple to slice (1 or 2): "))
            start = int(input("\nEnter the start index for slicing: "))
            end = int(input("\nEnter the end index for slicing: "))

            if tuple_choice == 1:
                sliced_tuple = Names1[start:end]
                print("Sliced tuple 1 is:",sliced_tuple)
            elif tuple_choice == 2:
                sliced_tuple = Names2[start:end]
                print("Sliced tuple 2 is:",sliced_tuple)
            else:
                print("Invalid tuple choice.")


        elif operation==7:
            tuple_choice=int(input("\nChoose which tuple to count the length(1 or 2)"))
            length_of_tuple=len(tuple_choice)
            print("Length of tuple is:",length_of_tuple)

    elif operation==8:
        print("Exit the program")
        break

    else:
        print("Invalid Choice..!!")