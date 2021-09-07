import sys
import re

re_yes = "[Yy]([Ee][Ss])?"
# There are 13 pay cycles in an ESPP period
pay_cycles = 13

# Assume the current stock price will be the price on upcoming purchase date
rpd_curr = float(input("What is the stock price today? "))
rpd_prev = float(input("What was the stock price at the beginning of this ESPP period? "))

y1 = float(input("How much $ do you contribute to ESPP per paycheck? "))

yn1 = input("Have you reduced your ESPP contribution in this period (y/N)? ")
if re.search(re_yes, yn1):

    x1 = int(input(f"On what paycheck did you reduce your contribution (1-{pay_cycles})? "))
    # The first contribution is #1. The last contribution is #26
    # +1 to account for range() method excluding the last value
    x1 = x1 if x1 in range(1, pay_cycles+1) else sys.maxsize

    y2 = float(input("How much $ is your reduced ESPP contribution per paycheck? "))

    yn2 = input("Have you reduced your ESPP contribution a second time to zero in this period (y/N)? ")
    if re.search(re_yes, yn2):
        x2 = int(input(f"On what paycheck cycle did you stop your ESPP contribution (2-{pay_cycles})? "))
        x2 = x2 if x2 in range(2, pay_cycles+1) else sys.maxsize
    else:
        # Contribution reduced only once
        x2 = pay_cycles
else:
    # No changes in contribution throughout the ESPP period
    x1 = sys.maxsize
    x2 = sys.maxsize
    y2 = 0

# The ESPP discount is 15% off the lower of either
# the closing price of the stock on the first day of this offering period, OR
# the closing price of the stock on the specified purchase date
rpd_purchase_price = min(rpd_prev, rpd_curr) * 0.85

# Initial contribution per paycheck elected during open enrollment * # of paychecks contributing this amount
# + decreased contribution per paycheck reduced during purchase period * # of paychecks contributing this amount
espp_contribution = min(x1, pay_cycles) * y1 + (x2 - x1) * y2

espp_purchase_value = espp_contribution / rpd_purchase_price * rpd_curr

print()
print(f"Your purchase price is\t${round(rpd_purchase_price, 2):.2f} per share")
print(f"You have contributed\t${round(espp_contribution, 2):.2f}")
print(f"Your purchase is worth\t${round(espp_purchase_value, 2):.2f}")
print(f"Your capital gains are\t${round(espp_purchase_value-espp_contribution, 2):.2f}")