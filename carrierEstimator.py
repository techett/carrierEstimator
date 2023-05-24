'''

carrierEstimator
Don't get burned again. Check before you sign!
By: Techett

'''


def plan_calculator(planCost, devicePayment, devicePromo, salesTax, carrier, term):
    '''
    Calculate the cost of a cellular service plan over a given term.

    Parameters:
    - planCost (float): Monthly cost of the plan.
    - devicePayment (float): Monthly payment for the device.
    - devicePromo (float): Promotional discount for the device. (orginalAmount minus the credit.)
    --> Example of devicePromo: devicePromo = 46.23 - 33.33 
    - salesTax (float): Tax rate applied to the plan and device payment.
    - carrier (str): Name of the cellular service provider.
    - term (int): Duration of the plan in months.

    Prints:
    - Monthly cost of the plan with tax included.
    --> This does not include local city / educational taxes. This is a rough estimate.
    --> Phone plans vary month to month. It is difficult to 100% accurately calculate surchages.
    - Total amount paid over the given term.

    '''

    # Variables
    months = 1
    effectiveDevicePayment = float(devicePayment - devicePromo)
    amountDue = float((planCost + effectiveDevicePayment) * salesTax)

    print(f"While on {carrier}, you can expect:")
    print(f"You will pay roughly: ${amountDue:.2f} every month.\n")

    while months <= term:
        totalPaid = amountDue * months
        print(
            f"You will have paid a total of: ${totalPaid:.2f} in {months} months.")
        months += 1

    print()  # Line break


# Examples

# planCost, devicePayment, devicePromo, salesTax, carrier, term(in months)
# plan_calculator(40, 0, 0, 1.06, "Spectrum Mobile", 6)
# plan_calculator(80, 46.25, 33.33, 1.06, "Verizon Mobile", 6)
