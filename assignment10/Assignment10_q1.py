import time
import random


class Bank:
    def __init__(self, bank_name, branch_name, ifsc_code ):
        self.bank_name = bank_name
        self.branch_name = branch_name
        self.ifsc_code = ifsc_code
        self.account_list = []

    def print_bank_details(self):
        print(f"Bank Name = {self.bank_name}")
        print(f"Branch Name = {self.branch_name}")
        print(f"IFSC Code = {self.ifsc_code}")

    def add_account(self, acc_holder_name ,mobile_number, acc_number):
        print(f"Account Created!\n Your Account Number is {acc_number}")
        self.account_list.append(Account(acc_holder_name ,mobile_number, acc_number))
        time.sleep(5)

    def print_account_details(self):
        for index in self.account_list:
            print(f"Account Holder Name = {index.acc_holder_name}")
            print(f"Mobile Number = {index.mobile_number}")
            print(f"Account Number = {index.acc_number}")
            print(f"Balance = {index.balance}")
            time.sleep(3)

    def delete_account(self, acc_number):
        for index in self.account_list:
            if index.acc_number == acc_number:
                self.account_list.remove(i)
                print(1)
                break
        else:
            print(0)

    def print_specific_account_details(self, acc_number):
        for index in self.account_list:
            if index.acc_number == acc_number:
                print(f"Account Holder Name = {index.acc_holder_name}")
                print(f"Mobile Number = {index.mobile_number}")
                print(f"Account Number = {index.acc_number}")
                print(f"Balance = {index.balance}")
                time.sleep(3)
                break
        else:
            print(f"Account Number is Not Valid")

    def return_acc_obj(self, acc_number):
        for index in self.account_list:
            if index.acc_number == acc_number:
                return index
                break
        else:
            return 1


class Account:
    def __init__(self, acc_holder_name ,mobile_number , acc_number):
        self.acc_holder_name = acc_holder_name
        self.mobile_number = mobile_number
        self.acc_number = acc_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Account Balance = {self.balance}")
        time.sleep(4)

    def withdraw(self, amount):
        if self.balance - amount < 3000:
            print(f"Minimum balance condition not met your balance is {self.balance}")
            time.sleep(3)
        else:
            self.balance -= amount
            print(f"Account Balance = {self.balance}")
            time.sleep(4)


bank1 = Bank('SBI', "Jalgaon", 444604)
while True:
    print(f"""\n====================Welcome To Banking Application===================\n1. Print Bank Details\n2. Add New User\n3. Print Information Of All Account\n4. Print Information of selected Account\n5. Delete Selected Account\n6. Deposit Amount\n7. Withdraw Amount\n8. Exit""")
    choice = int(input("\nEnter Your Choice\n"))
    if choice == 1:
        bank1.print_bank_details()

    elif choice == 2:
        acc_holder_name = input("Enter Account Holder Name")
        mobile_number = int(input("Enter Mobile Number"))
        acc_number = random.randrange(10000,99999)
        # acc_number = int(input("Enter Account Number"))
        bank1.add_account(acc_holder_name, mobile_number, acc_number)

    elif choice == 3:
        bank1.print_account_details()

    elif choice == 4:
        acc_number = int(input("Enter Account Number"))
        bank1.print_specific_account_details(acc_number)

    elif choice == 5:
        acc_number = int(input("Enter Account Number"))
        bank1.delete_account(acc_number)

    elif choice == 6:
        acc_number = int(input("Enter Account Number"))
        amount = int(input("Enter Amount to be deposited"))
        if bank1.return_acc_obj(acc_number) == 1:
            print(f"Not A Valid Account Number")
            time.sleep(3)
        else:
            bank1.return_acc_obj(acc_number).deposit(amount)

    elif choice == 7:
        acc_number = int(input("Enter Account Number"))
        amount = int(input("Enter Amount to be deposited"))
        if bank1.return_acc_obj(acc_number) == 1:
            print(f"Not A Valid Account Number")
            time.sleep(3)
        else:
            bank1.return_acc_obj(acc_number).withdraw(amount)

    elif choice == 8:
        break

