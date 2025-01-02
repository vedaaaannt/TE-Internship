#List 1
Fruits=['Apple','Banana','Orange','Guava','Pineapple','Watermelon']
                             # Initializing List
print(Fruits)                # Printing list
print(len(Fruits))           # Printing Length of the list                          Function1 len()

Fruits.reverse()             # Reversing the order of Objects in the list           Function2 .reverse()
print(Fruits)

#List 2
VehicleBrands=['BMW','Porsche','Toyota','Tata','Mclaren']
                             # Initializing List
print(VehicleBrands)         # Printing list
VehicleBrands.insert(2,'Ferrari')
                             # Inserting new Object to the list                     Function3 .insert()
print(VehicleBrands)
print(len(VehicleBrands))    # Printing Length of the list

Fruits.extend(VehicleBrands) # Merging the both lists                               Function4 .extend()
print(Fruits)                # Fruits + VehicleBrands = Fruits

Fruits.pop(5)                # Removing object Apple from the list                  Function5 .pop()
print(Fruits)                # Printing the updated list

Fruits.append('Apple')       # Adding object "Apple" at the end of the list         Function6 .append()
print(Fruits)                # Printing the updated list
print(len(Fruits))           # Printing Length of the New list

C=Fruits.count("Tata")       # Count of appearance of object "Tata"                 Function7 .count()
print(C)                     # Print the Count

Fruits.clear()               # Clearing the overall list                            Function8 .clear()
print(Fruits)                # Printing the Final list



#Set function