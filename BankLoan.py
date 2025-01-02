print("Welcome To SBI Bank..!!!")
print("1.Home Loan")
print("2.Car Loan")
print("3.Education Loan")
print("4.Exit")

ch=int(input("Enter Your choice:"))

if ch==1:
    print("Offering Home Loan on 12% interest..!!")

elif ch==2:
    print("Offering Car Laon on 12% interest..!!")

elif ch==3:
    print("Offering Education Loan on 12% interest..!!")

else:
    print("Invalid choice")
    #continue

continue_choice = input("Do you want to proceed and enter loan amount? (yes/no): ")
if continue_choice == 'yes':
    print("You required documents like Aadhar card,Bank Passbook,Photo")

    loan_amount = float(input("Enter the loan amount: "))
    print("Your loan amount is:",loan_amount)

    monthly_salary=float(input("Enter your monthly salary:"))
    print("Your Salary amount is:",monthly_salary)

    loan_tenure = int(input("Enter the loan tenure in years: "))
    annual_interest_rate = 12


    if loan_amount<=(monthly_salary*3):
        print("Your loan has been approved!")
    else:
        print("Sorry, your loan is not approved because your salary is Less.")

        interest_rate=0.12
        emi=loan_amount*interest_rate/12
        print("Your Emi is on 12% interest is:",emi)
else:
    print("Not Proceed")