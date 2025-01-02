print("---------------- Operator Menu ----------------")
print("1 .Addition of two no.s")
print("2. Subtraction of two no.s")
print("3. Multiplication of two no.s")
print("4. Division(Float Method) of two no.s")
print("5. Division(Floor Method) of two no.s")
print("6. Remainder of two no.s (Modulus Operator)")
print("7. Power operator(a^b)")
print("8. Add AND Operator(a+=b)")
print("9. Subtract AND Operator(a-=b)")
print("10. Multiply AND Operator(a*=b)")
print("11. Division AND Operator(a/=b)")
print("12. Modulus AND Operator(a%=b)")
print("13. Bitwise AND Operator(a&b)")
print("14. Bitwise OR Operator(a|b)")
print("15. Comparison Operator(Equal to)")

choice = int(input("Enter the choice:"))

if choice in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
    a=int(input("Enter the value of 1st No.: "))
    b=int(input("Enter the value of 2nd No.: "))

    if choice == 1 :
        c = a + b
        print("Result: ",c)

    elif choice == 2 :
        c = a - b
        print("Result: ",c)

    elif choice == 3:
        c = a * b
        print("Result: ", c)

    elif choice == 4:
        c = a / b
        print("Result: ", c)

    elif choice == 5:
        c = a // b
        print("Result: ", c)

    elif choice == 6:
        c = a % b
        print("Result: ", c)

    elif choice == 7 :
        c = a ** b
        print("Result: ", c)

    elif choice == 8 :
        a+=b
        print("Result: ", a)

    elif choice == 9 :
        a-=b
        print("Result: ", a)

    elif choice == 10 :
        a*=b
        print("Result: ", a)

    elif choice == 11:
        a/=b
        print("Result: ", a)

    elif choice == 12 :
        a%=b
        print("Result: ", a)

    elif choice == 13 :
        a&=b
        print("Result: ", a)

    elif choice == 14 :
        a|=b
        print("Result: ", a)

    elif choice == 15 :
        if a==b:
            print("Value of both the no.s is Equal")
        else:
            print("value of both the no.s is Distinct")

else:
    print("!!Invalid Choice!!")