import sys
import re
import math

re_yes = "[Yy]([Ee][Ss])?"
# There are 13 pay cycles in an ESPP period
pay_cycles = 13

# Assume the current stock price will be the price on upcoming purchase date
rpd_curr = float(input("What is the stock price today? $"))
rpd_prev = float(input("What was the stock price at the beginning of this ESPP period? $"))

y1 = float(input("How much $ do you contribute to ESPP per paycheck? $"))

yn1 = input("Have you reduced your ESPP contribution in this period (y/N)? ")
if re.search(re_yes, yn1):

    x1 = int(input(f"On what paycheck did you reduce your contribution (1-{pay_cycles})? "))
    # The first contribution is #1. The last contribution is #26
    # +1 to account for range() method excluding the last value
    x1 = x1 if x1 in range(1, pay_cycles+1) else sys.maxsize

    y2 = float(input("How much $ is your reduced ESPP contribution per paycheck? $"))

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

prev_carry_forward = float(input("How much $ is carrying forward from a previous ESPP purchase period? $"))

# The ESPP discount is 15% off the lower of either
# the closing price of the stock on the first day of this offering period, OR
# the closing price of the stock on the specified purchase date
# ESPP rounds purchase price per share to the nearest penny
rpd_purchase_price = round((min(rpd_prev, rpd_curr) * 0.85), 2)

# Initial contribution per paycheck elected during open enrollment * # of paychecks contributing this amount
# + decreased contribution per paycheck reduced during purchase period * # of paychecks contributing this amount
# + amount rolled over from previous purchase period
espp_contribution = min(x1, pay_cycles) * y1 + (x2 - x1) * y2 + prev_carry_forward

rpd_shares = math.floor(espp_contribution / rpd_purchase_price)

espp_purchase_price = rpd_shares * rpd_purchase_price
espp_purchase_value = rpd_shares * rpd_curr

espp_carry_forward = espp_contribution - espp_purchase_price
taxable_gain = espp_purchase_value - espp_purchase_price

print()
print(f"You have contributed\t${espp_contribution:.2f} to this ESPP period")
print(f"Your purchase price is\t${rpd_purchase_price:.2f} per share")
print(f"You have purchased\t{rpd_shares} shares of RPD")
print(f"For a total price of\t${espp_purchase_price:.2f}")
print(f"You have remaining\t${espp_carry_forward:.2f} carrying forward to the next ESPP period")
print(f"Your purchase is worth\t${espp_purchase_value:.2f} today")
print(f"Your taxable gain is\t${taxable_gain:.2f}")
