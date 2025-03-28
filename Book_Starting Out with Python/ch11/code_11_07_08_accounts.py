# The SavingsAccount class represents a savings account
class SavingsAccount:
    # The __init__ method accepts arguments for the account number, interest rate, and balance.
    def __init__(self, account_num, int_rate, bal):
        self.__account_num = account_num
        self.__interest_rate = int_rate
        self.__balance = bal

    # The following methods are mutators for the data attributes
    def self_account_num(self, account_num):
        self.__account_num = account_num

    def self_interest_rate(self, int_rate):
        self.__interest_rate = int_rate

    def self_balance(self, bal):
        self.__balance = bal

    # The following methods are accessors for the data attributes
    def get_account_num(self):
        return self.__account_num
    
    def get_interest_rate(self):
        return self.__interest_rate
    
    def get_balance(self):
        return self.__balance
    
# The CD account represents a certificate of deposit (CD) account. It is a subclass of the SavingsAccount class.
class CD(SavingsAccount):
    # the init method accepts arguments for account number, interest rate, balance, and matureity date.
    def __init__(self, account_num, int_rate, bal, mat_date):
        # Call the superclass __init__ mehtod
        SavingsAccount.__init__(self, account_num, int_rate, bal)

        # Initialize the __maturity_date attribute
        self.__maturity_date = mat_date

    # the set_maturity_date is a mutator for the __maturity_date attribute.
    def set_maturity_date(self, mat_date):
        self.__maturity_date = mat_date

    # the get_maturity_date method is an accessor for the __maturity_date attribute
    def get_maturity_date(self):
        return self.__maturity_date