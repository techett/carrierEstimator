from carrierEstimator import plan_calculator

# Input parameters
plan_cost = 40
device_payment = 0
device_promo = 0
sales_tax = 1.06
carrier = "Spectrum Mobile"
term = 6

# Calculate plan cost and total amount paid
plan_calculator(plan_cost, device_payment,
                device_promo, sales_tax, carrier, term)
