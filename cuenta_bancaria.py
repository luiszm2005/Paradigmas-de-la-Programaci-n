from typing import List
import os
os.system("cls")

class BankAccount:
    # Initializes the bank account with a holder and an initial balance
    # Both attributes are private
    def __init__(self, headline: str, balance: float = 0.0) -> None:
        self.__headline: str = headline
        self.__balance: float = balance
        
    # Getter method for balance
    def get_balance(self) -> float:
        return self.__balance
    
    # Setter method for balance
    def set_balance(self, balance: float) -> None:
        self.__balance = balance
        
    # Getter method for headline
    def get_headline(self) -> str:
        return self.__headline
    
    # Setter method for headline
    def set_headline(self, headline: str) -> None:
        self.__headline = headline
        
        
    def deposit(self, quantity: float) -> None:
    # Adds an amount to the account balance if the amount is greater than zero.
        if quantity > 0:
            self.__balance += quantity
            print("Successful deposit. New balance:", self.__balance)
        else:
            print("The amount to be deposited must be greater than zero.")
            
    def withdraw(self, quantity: float) -> None:
    # Subtracts an amount from the account balance if there are sufficient funds and the amount is greater than zero.
        if quantity > 0:
            if self.__balance >= quantity:
                self.__balance -= quantity
                print("Successful retirement. New balance sheet:", self.__balance)
            else:
                print("Insufficient funds to make the withdrawal.")
        else:
            print("The amount to be withdrawn must be greater than zero.")
        
    def check_balance(self) -> None:
    # Prints the current balance of the account.
        print(f"Your balance is: {self.get_balance()}")
        
    def check_headline(self) -> None:
    # Prints the name of the account holder.
        print(f"Its owner is: {self.get_headline()}")
        
# Create an account for an account holder
headline = input("Enter the holder's name: ")  # Requests the name of the holder from the user
account = BankAccount(headline)  # Create a new bank account with the name of the account holder.

# Deposit
deposit_quantity = float(input("How much would you like to deposit? "))  # Requests the amount to be deposited
account.deposit(deposit_quantity)  # Make the deposit in the account

# Withdraw
withdrawal_quantity = float(input("How much would you like to withdraw? "))  # Request the amount to be withdrawn
account.withdraw(withdrawal_quantity)  # Make the withdrawal from the account

# Check Balance
account.check_balance()  # Prints the current account balance

# Consult headline
account.check_headline()  # Prints the account holder's name