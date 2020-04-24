import math


class CreditCalculator:
    def __init__(self):
        self.chosen_one = None

        self.credit_principal = None
        self.monthly_payment = None
        self.credit_interest = None
        self.count_of_periods = None

        self.mth_diff_payment = None
        self.sum_of_diff_payments = None
        self.month = None

        self.invalid = "You gave an invalid input, please verify."

    def asker(self):
        if not self.chosen_one:
            print('What do you want to calculate?')
            print('  type "n" - for count of months,')
            print('  type "a" - for annuity monthly payment,')
            print('  type "p" - for credit principal,')
            print('  type "d" - for differentiated monthly payment:')
            print('>', end=" ")

            self.chosen_one = input()

            return self.input_validator()
        elif self.chosen_one == "n":
            while self.credit_principal is None:
                print("Enter credit principal:\n>", end=" ")
                self.credit_principal = input()
                self.input_validator("credit_principal")
            while self.monthly_payment is None:
                print("Enter monthly payment:\n>", end=" ")
                self.monthly_payment = input()
                self.input_validator("monthly_payment")
            while self.credit_interest is None:
                print("Enter credit interest:\n>", end=" ")
                self.credit_interest = input()
                self.input_validator("credit_interest")

            return self.count_of_period_calc()
        elif self.chosen_one == "a":
            while self.credit_principal is None:
                print("Enter credit principal:\n>", end=" ")
                self.credit_principal = input()
                self.input_validator("credit_principal")
            while self.count_of_periods is None:
                print("Enter count of periods:\n>", end=" ")
                self.count_of_periods = input()
                self.input_validator("count_of_periods")
            while self.credit_interest is None:
                print("Enter credit interest:\n>", end=" ")
                self.credit_interest = input()
                self.input_validator("credit_interest")

            return self.monthly_payment_calc()
        elif self.chosen_one == "p":
            while self.monthly_payment is None:
                print("Enter monthly payment:\n>", end=" ")
                self.monthly_payment = input()
                self.input_validator("monthly_payment")
            while self.count_of_periods is None:
                print("Enter count of periods:\n>", end=" ")
                self.count_of_periods = input()
                self.input_validator("count_of_periods")
            while self.credit_interest is None:
                print("Enter credit interest:\n>", end=" ")
                self.credit_interest = input()
                self.input_validator("credit_interest")

            return self.credit_principal_calc()
        else:
            while self.credit_principal is None:
                print("Enter credit principal:\n>", end=" ")
                self.credit_principal = input()
                self.input_validator("credit_principal")
            while self.count_of_periods is None:
                print("Enter count of periods:\n>", end=" ")
                self.count_of_periods = input()
                self.input_validator("count_of_periods")
            while self.credit_interest is None:
                print("Enter credit interest:\n>", end=" ")
                self.credit_interest = input()
                self.input_validator("credit_interest")

            return self.mth_diff_payment_calc()

    def input_validator(self, question=None):
        if question is None:
            if self.chosen_one in ("n", "a", "p", "d"):
                return self.asker()
            else:
                print(self.invalid)
                self.chosen_one = None
                return self.asker()
        else:
            if question == "credit_principal":
                try:
                    self.credit_principal = float(self.credit_principal)
                except TypeError:
                    print(self.invalid)
                    self.credit_principal = None
            elif question == "monthly_payment":
                try:
                    self.monthly_payment = float(self.monthly_payment)
                except TypeError:
                    print(self.invalid)
                    self.monthly_payment = None
            elif question == "credit_interest":
                try:
                    self.credit_interest = float(self.credit_interest)
                except TypeError:
                    print(self.invalid)
                    self.credit_interest = None
            elif question == "count_of_periods":
                try:
                    self.count_of_periods = float(self.count_of_periods)
                except TypeError:
                    print(self.invalid)
                    self.count_of_periods = None

    def count_of_period_calc(self):
        try:
            nominal_monthly_interest = (self.credit_interest / 100) / (12 * 1)
            count_of_months = (math.log((self.monthly_payment / (self.monthly_payment
                                                                 - (nominal_monthly_interest
                                                                    * self.credit_principal))
                                         ), (1 + nominal_monthly_interest)))
        except ValueError:
            return self.answer_printer(False)
        count_of_months = math.ceil(count_of_months)
        self.count_of_periods = [count_of_months // 12, math.ceil(count_of_months % 12)]  # year(s), month(s)
        self.answer_printer()

        self.count_of_periods = count_of_months
        self.overpayment_calc()

    def monthly_payment_calc(self):
        try:
            nominal_monthly_interest = (self.credit_interest / 100) / (12 * 1)
            self.monthly_payment = (self.credit_principal
                                    * ((nominal_monthly_interest
                                        * ((1 + nominal_monthly_interest)
                                           ** self.count_of_periods)) / (((1 + nominal_monthly_interest)
                                                                          ** self.count_of_periods) - 1)))
        except ArithmeticError:
            return self.answer_printer(False)
        self.monthly_payment = math.ceil(self.monthly_payment)
        self.answer_printer()

        self.overpayment_calc()

    def credit_principal_calc(self):
        try:
            nominal_monthly_interest = (self.credit_interest / 100) / (12 * 1)
            self.credit_principal = (self.monthly_payment
                                     / ((nominal_monthly_interest
                                         * ((1 + nominal_monthly_interest)
                                            ** self.count_of_periods)) / (((1 + nominal_monthly_interest)
                                                                           ** self.count_of_periods) - 1)))
        except ArithmeticError:
            return self.answer_printer(False)
        self.credit_principal = math.floor(self.credit_principal)
        self.answer_printer()

        self.overpayment_calc()

    def mth_diff_payment_calc(self):
        try:
            nominal_monthly_interest = (self.credit_interest / 100) / (12 * 1)
        except ArithmeticError:
            return self.answer_printer(False)
        self.sum_of_diff_payments = 0
        for self.month in range(1, math.ceil(self.count_of_periods) + 1):
            try:
                self.mth_diff_payment = ((self.credit_principal / self.count_of_periods)
                                         + (nominal_monthly_interest
                                            * (self.credit_principal
                                               - ((self.credit_principal
                                                   * (self.month - 1)) / self.count_of_periods))))
            except ArithmeticError:
                return self.answer_printer(False)
            self.mth_diff_payment = math.ceil(self.mth_diff_payment)
            self.sum_of_diff_payments += self.mth_diff_payment
            self.answer_printer()

        self.overpayment_calc()

    def answer_printer(self, possible=True):
        if not possible:
            print("It is impossible to calculate, please check the entered numbers.")
            print(f"Credit principal: {self.credit_principal or 'Not specified / Sought'},", end=" ")
            print(f"Monthly payment: {self.monthly_payment or 'Not specified / Sought'},", end=" ")
            print(f"Credit interest: {self.credit_interest or 'Not specified / Sought'},", end=" ")
            print(f"Count of periods: {self.count_of_periods  or 'Not specified / Sought.'}")
            self.__init__()
            self.asker()
        elif self.chosen_one == "n":
            if self.count_of_periods[0] == 0:
                if self.count_of_periods[1] == 1:
                    print(f"You need {self.count_of_periods[1]} month to repay this credit!")
                else:
                    print(f"You need {self.count_of_periods[1]} months to repay this credit!")
            elif self.count_of_periods[0] == 1:
                if self.count_of_periods[1] == 0:
                    print(f"You need {self.count_of_periods[0]} year to repay this credit!")
                elif self.count_of_periods[1] == 1:
                    print(f"You need {self.count_of_periods[0]} year and", end=" ")
                    print(f"{self.count_of_periods[1]} month to repay this credit!")
                else:
                    print(f"You need {self.count_of_periods[0]} year and", end=" ")
                    print(f"{self.count_of_periods[1]} months to repay this credit!")
            else:
                if self.count_of_periods[1] == 0:
                    print(f"You need {self.count_of_periods[0]} years to repay this credit!")
                elif self.count_of_periods[1] == 1:
                    print(f"You need {self.count_of_periods[0]} years and", end=" ")
                    print(f"{self.count_of_periods[1]} month to repay this credit!")
                else:
                    print(f"You need {self.count_of_periods[0]} years and", end=" ")
                    print(f"{self.count_of_periods[1]} moths to repay this credit!")
        elif self.chosen_one == "a":
            print(f"Your annuity payment = {self.monthly_payment}!")
        elif self.chosen_one == "p":
            print(f"Your credit principal = {self.credit_principal}!")
        else:
            print(f"Month {self.month}: paid out {self.mth_diff_payment}")

    def overpayment_calc(self):
        if self.chosen_one == "d":
            overpayment = self.sum_of_diff_payments - self.credit_principal
            overpayment = math.ceil(overpayment)
            print("")
            self.overpayment_printer(overpayment)
        else:
            overpayment = (self.monthly_payment * self.count_of_periods) - self.credit_principal
            overpayment = math.ceil(overpayment)
            self.overpayment_printer(overpayment)

    @staticmethod
    def overpayment_printer(overpayment):
        print(f"Overpayment = {overpayment}")


credit_calculator = CreditCalculator()
