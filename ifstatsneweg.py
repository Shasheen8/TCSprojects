# '''price of a house is $1M
# if buyer has good credit,
# they put down payment 10%
# otherwise
# they need to put 20%
# print the payment'''
price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment} ")
