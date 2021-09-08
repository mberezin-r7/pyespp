# PyESPP

Calculate ESPP value based on paycheck contributions.

## Introduction

This script helps calculate the expected values of Purchase Details fields as they appear on the Employee Stock Plan Purchase Confirmation document that one receives at the end of an ESPP period.

## How to use

You need Python installed to run this script. It has no dependencies outside of the standard library.

Simply run the script with `python espp.py` and fill in the prompts.

## FAQ

### Where can I find my Employee Stock Plan Purchase Confirmation documents?

Log in to ETRADE. Go to Stock Plan > My Account > Stock Plan Confirmations. Click Download on the rows where Benefit Type = ESPP.

### What field does each prompt and result variable correspond to?

#### Where to find values for the prompts

`What is the stock price today?` = Purchase Confirmation > Purchase Details > Calculation of Shares Purchased > Purchase Value per Share

`What was the stock price at the beginning of this ESPP period?` = Purchase Confirmation > Purchase Details > Calculation of Shares Purchased > Grant Date Market Value

`How much do you contribute to ESPP per paycheck?` = Pay Statement > Deductions > Other > ESPP$

`How much $ is carrying forward from a previous ESPP purchase period?` = Purchase Confirmation > Purchase Details > Contributions > Previous Carry Forward

#### What each result value corresponds to

`You have contributed $X to this ESPP period` = Purchase Confirmation > Purchase Details > Contributions > Total Contributions

`Your purchase price is $X per share` = Purchase Confirmation > Purchase Details > Calculation of Shares Purchased > Purchase Price per Share (85% of $Y)

`You have purchased X shares of RPD` = Purchase Confirmation > Purchase Summary > Shares Purchased to Date in Current Offering > Shares Purchased

`For a total price of $X` = Purchase Confirmation > Purchase Details > Total Price

`You have remaining $X carrying forward to the next ESPP period` = Purchase Confirmation > Purchase Details > Carry Forward

`Your purchase is worth $X today` = Purchase Confirmation > Purchase Details > Calculation of Gain > Total Value

`Your taxable gain is $X`  = Purchase Confirmation > Purchase Details > Calculation of Gain > Taxable Gain

### How do I input my final total ESPP contribution for this period, instead of my contribution per paycheck?

Let `X` be your final total ESPP contribution for this period. Enter the following responses to each prompt.

```
How much $ do you contribute to ESPP per paycheck? $X
Have you reduced your ESPP contribution in this period (y/N)? YES
On what paycheck did you reduce your contribution (1-13)? 1
How much $ is your reduced ESPP contribution per paycheck? $0
Have you reduced your ESPP contribution a second time to zero in this period (y/N)? NO
How much $ is carrying forward from a previous ESPP purchase period? $0
```