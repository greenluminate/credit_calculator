import argparse
from _credit_calculator import CreditCalculator


class CMDCreditCalculator(CreditCalculator):
    def __init__(self):
        super().__init__()
        self.incorrect = "Incorrect parameter"
        self.help = "Use -h to get help."

    def cmd_args_parser(self):
        parser = argparse.ArgumentParser()

        parser.add_argument("--type", default=None,
                            help="--type must be given to use the script. Please input 'diff' or 'annuity'.")
        parser.add_argument("--principal", default=None,
                            help="Input an integer or a float number.")
        parser.add_argument("--periods", default=None,
                            help="Input a positive integer or a float number.")
        parser.add_argument("--interest", default=None,
                            help="--interest must be given to use the script. Please input a number.")
        parser.add_argument("--payment", default=None,
                            help="Input an integer or a float number.")

        args = parser.parse_args()
        self.cmd_args_validator(args)

    def cmd_args_validator(self, args):
        if args.interest is None:
            return print(f"Did not get --interest parameter. {self.help}")
        else:
            try:
                self.credit_interest = float(args.interest)
            except ValueError:
                return print(f"{self.incorrect} for --interest {self.help}")

        if args.type == "diff":
            self.chosen_one = "d"
            try:
                self.credit_principal = float(args.principal)
                self.count_of_periods = float(args.periods)
            except ValueError:
                return print(f"{self.incorrect}(s) for differentiate calculation. {self.help}")
            if self.count_of_periods <= 0:
                return print(f"Got {self.incorrect} for periods.")
            return self.mth_diff_payment_calc()

        elif args.type == "annuity":
            if args.principal is None or args.payment is None:
                pass
            else:
                self.chosen_one = "n"
                try:
                    self.credit_principal = float(args.principal)
                    self.monthly_payment = float(args.payment)
                except ValueError:
                    return print(f"{self.incorrect}(s) for period calculation. {self.help}")
                return self.count_of_period_calc()

            if args.principal is None or args.periods is None:
                pass
            else:
                self.chosen_one = "a"
                try:
                    self.credit_principal = float(args.principal)
                    self.count_of_periods = float(args.periods)
                except ValueError:
                    return print(f"{self.incorrect}(s) for monthly payment calculation. {self.help}")
                if self.count_of_periods <= 0:
                    return print(f"Got {self.incorrect} for periods.")
                return self.monthly_payment_calc()

            if args.payment is None or args.periods is None:
                pass
            else:
                self.chosen_one = "p"
                try:
                    self.monthly_payment = float(args.payment)
                    self.count_of_periods = float(args.periods)
                except ValueError:
                    return print(f"{self.incorrect}(s) for credit principal calculation. {self.help}")
                if self.count_of_periods <= 0:
                    return print(f"Got {self.incorrect} for periods.")
                return self.credit_principal_calc()

            print("Did not get the right combination of parameters to calculate anything.")
            print("Try the following text based calculator:")

        else:
            print(f"{self.incorrect} for --type. {self.help}")


cmd_credit_calculator = CMDCreditCalculator()
