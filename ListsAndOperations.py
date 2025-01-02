dynamiclist = []
dynamiclist2 = []

while True:
    print("--------------- Menu ---------------")
    print("1. Access Lists")
    print("2. Operation on Lists")
    print("3. Exit Program")

    choice = int(input("Enter Choice:"))
    if choice in [1,2,3]:
        if choice == 1:
            while True:
                CHOICE = int(input("Enter which list to perform work on(1/2): "))
                if CHOICE in [1,2]:

                    #----------------------------------------------- LIST 1 -----------------------------------------------
                    if CHOICE == 1:
                        while True:
                            print("--------------- List 1 Menu ---------------")
                            print("1. Add/Insert element to the list")
                            print("2. Delete/Remove element from the list")
                            print("3. Check the size/length of the list")
                            print("4. Print/Show the current list")
                            print("5. Reverse the current list")
                            print("6. Check for the repetition of any object in the list")
                            print("7. Clear the list")
                            print("8. Exit")

                            choice = int(input("Enter the choice: "))

                            if choice in [1,2,3,4,5,6,7,8]:

                                if choice == 1:
                                    element=input("Enter the element to be added in the list: ")
                                    dynamiclist.append(element)
                                    print("Element is added to the list.")
                                    print("Current List:", dynamiclist)

                                elif choice == 2:
                                    element = int(input("Enter the element to be removed from the list: "))
                                    if element in dynamiclist:
                                        dynamiclist.pop(element)
                                        print("Element is removed from the list.")
                                        print("Current List:", dynamiclist)

                                    else:
                                        print("Element is not present in the list.")
                                        print("Current List:", dynamiclist)

                                elif choice == 3:
                                    print("Size/Length of the list is: ",len(dynamiclist))

                                elif choice == 4:
                                    print("Current List:", dynamiclist)

                                elif choice == 5:
                                    dynamiclist.reverse()
                                    print("Current List:", dynamiclist)

                                elif choice == 6:
                                    element=input("Enter the Element:")
                                    c=dynamiclist.count(element)
                                    print("No. of time's the element appear in the list is: ",c)

                                elif choice == 7:
                                    dynamiclist.clear()
                                    print("Current List:", dynamiclist)

                                elif choice == 8:
                                    print("Exiting List 1")
                                    break

                                else:
                                    print("Invalid choice please try again!!")

                    #----------------------------------------------- LIST 2 -----------------------------------------------
                    elif CHOICE == 2:
                        while True:
                            print("---------------List 2 Menu ---------------")
                            print("1. Add/Insert element to the list")
                            print("2. Delete/Remove element from the list")
                            print("3. Check the size/length of the list")
                            print("4. Print/Show the current list")
                            print("5. Reverse the current list")
                            print("6. Check for the repetition of any object in the list")
                            print("7. Clear the list")
                            print("8. Exit")

                            choice = int(input("Enter the choice: "))

                            if choice in [1,2,3,4,5,6,7,8]:

                                if choice == 1:
                                    element=input("Enter the element to be added in the list: ")
                                    dynamiclist2.append(element)
                                    print("Element is added to the list.")
                                    print("Current List:", dynamiclist2)

                                elif choice == 2:
                                    element = int(input("Enter the element to be removed from the list: "))
                                    if element in dynamiclist2:
                                        dynamiclist2.pop(element)
                                        print("Element is removed from the list.")
                                        print("Current List:", dynamiclist2)

                                    else:
                                        print("Element is not present in the list.")
                                        print("Current List:", dynamiclist2)

                                elif choice == 3:
                                    print("Size/Length of the list is: ",len(dynamiclist2))

                                elif choice == 4:
                                    print("Current List:", dynamiclist2)

                                elif choice == 5:
                                    dynamiclist2.reverse()
                                    print("Current List:", dynamiclist2)

                                elif choice == 6:
                                    element=input("Enter the Element:")
                                    c=dynamiclist2.count(element)
                                    print("No. of time's the element appear in the list is: ",c)

                                elif choice == 7:
                                    dynamiclist2.clear()
                                    print("Current List:", dynamiclist2)

                                elif choice == 8:
                                    print("Exiting List 2")
                                    break

                                else:
                                    print("Invalid choice please try again!!")



                else:
                    print("Invalid choice!! Exiting operation.")
                    break

        elif choice == 2:
            while True:
                print("Operations:")
                print("1. Compare both lists")
                print("2. Merge both lists")
                print("3. Exit")

                CHOICE = int(input("Enter Choice:"))
                while True:
                    if CHOICE in [1,2,3]:
                        x = set(dynamiclist)
                        y = set(dynamiclist2)
                        if CHOICE == 1:

                            if x == y:
                                print("Both lists have same elements.")
                                print("List 1:",dynamiclist)
                                print("List 2:",dynamiclist2)
                                break

                            elif x != y:
                                print("Both lists are not equal.")
                                if x > y:
                                    print("Overall value of List 1 is greater than overall value of List 2")
                                    print("List 1:", dynamiclist)
                                    print("List 2:", dynamiclist2)

                                else:
                                    print("Overall value of List 1 is lesser than overall value of List 2")
                                    print("List 1:", dynamiclist)
                                    print("List 2:", dynamiclist2)

                                break

                        elif CHOICE == 2:
                            print("List 1:", x)
                            print("List 2:", y)
                            dynamiclist.extend(dynamiclist2)
                            print("Extended List: ",dynamiclist)
                            break

                        elif CHOICE == 3:
                            print("Exiting Operation.")
                            break

                break



        elif choice == 3:
            print("Exiting Program!")
            break