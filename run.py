from carrierEstimator import plan_calculator

# Input parameters
'''
plan_cost: more commonly known as line fee. 
Ex: 45 line fee
~~~

device_payment: payment for the data service provided by your mobile operator (if any).
Ex: an iPhone 14 may cost 27.99 per month
~~~

device_promo: how much should be deducted from your monthly cost
Ex: You traded in an iphone 11 for the 14 and got a promo/credit for $400 at $10 off every month.
The $10 would be deducted from your device_payment
~~~

sales_tax: what percentage of revenue goes to taxes? 
Ex: In Kentucky it's 6%
~~~

carrier: name or branding of your cellular provider
~~~

term: How long will you be paying off this device?

'''

plan_cost = 40 
device_payment = 0
device_promo = 0
sales_tax = 1.06
carrier = "Spectrum Mobile"
term = 6

# Calculate plan cost and total amount paid
plan_calculator(plan_cost, device_payment,
                device_promo, sales_tax, carrier, term)
