import sys
from _credit_calculator import credit_calculator
from _cmd_credit_calculator import cmd_credit_calculator

if not sys.argv[:-1]:
    credit_calculator.asker()
else:
    cmd_credit_calculator.cmd_args_parser()
