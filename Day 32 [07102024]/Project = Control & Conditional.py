import random
accounts = {
        112233 : [1234,"Vardhan","7893570611",10000],
        445566 : [5678,"Vivek","923456788",20000],
        778899 : [2408,"Sai Vardhan","9123456787",50000]
    }

while True:
    print("ATM Menu")
    print("Choose the Required Option(s): ")
    print("1. Check Balanace ")
    print("2. Deposit ")
    print("3. Withdraw ")
    print("4. Pin change")
    print("5. Pin Generation")
    print("6. Exit")
    option = int(input("choose Your Option : "))
    if option == 1:
        accno = int(input("Enter your Account Number: "))
        if accno not in accounts:
            print("Account does not exists !")
        else:
            pin = int(input("Enter Pin: "))
            if pin != accounts[accno][0]:
                print("Invalid Pin")
            else:
                print(f"Balance : {accounts[accno][3]}")
    elif option == 2:
        accno = int(input("Enter your Account Number: "))
        if accno not in accounts:
            print("Account does not exists !")
        else:
            money = int(input("Enter amount to Deposit: "))
            accounts[accno][3] += money
            print("Money Deposited Sucesfully !")
    elif option == 3:
        accno = int(input("Enter your Account Number: "))
        if accno not in accounts:
            print("Account does not exists !")
        else:
            pin = int(input("Enter Pin: "))
            if pin != accounts[accno][0]:
                print("Invalid Pin")
            else:
                money = int(input("Enter Amount to Withdraw: "))
                if money >= accounts[accno][3]:
                    print("Insufficient Funds !..")
                else:
                    print("Collect your cash....")
                    accounts[accno][3] -= money
    elif option == 4:
        accno = int(input("Enter your Account Number: "))
        if accno not in accounts:
            print("Account does not exists !")
        else:
            pin = int(input("Enter Pin: "))
            if pin != accounts[accno][0]:
                print("Invalid Pin")
            else:
                npin = int(input("Enter New pin: "))
                cpin = int(input("confirm new pin: "))
                if npin != cpin:
                    print("Pin change Failed")
                else:
                    accounts[accno][0] = npin
                    print("Pin Changed Sucessfully ..")
    elif option == 5:
        accno = random.randint(111111,999999)
        print(f"Note Your Account Number - {accno}.")
        pin = int(input("Create a New Pin: "))
        cpin = int(input("Confirm your new pin: "))
        if pin != cpin:
            print("Account Generation Failed")
        else:
            name = input("Enter your name: ")
            mobile = input("Enter your Mobile number: ")
            accounts[accno] = [pin,name,mobile,0]
            print("Account and Pin Generated sucessfully...")
    else:
        print("Thanks for using ATM")
        break




        
