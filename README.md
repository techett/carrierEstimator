# carrierEstimator

## Introduction
The `carrierEstimator` tool is designed to simplify the process of shopping for phone plans and estimating their costs. Say goodbye to manually comparing phone plans and losing money on unfavorable deals. With `carrierEstimator`, you can quickly and easily compare different phone plans based on your specific needs and preferences.

## Usage
To estimate the cost of a phone plan using `carrierEstimator`, you need to provide the following information:
- Plan cost/Line fee: The monthly cost of the phone plan.
- Device payment cost: The monthly payment for the device.
- Promotion amount for device: The promotional discount applied to the device payment.
- Sales tax for your state: The sales tax rate applicable to the plan and device payment.
- Name of carrier: The name of the cellular service provider.
- Duration of device payment agreement/contract: The number of months for the device payment agreement.

Example usage:
```python
from carrierEstimator import plan_calculator

# Input parameters
plan_cost = 40
device_payment = 0
device_promo = 0
sales_tax = 1.06
carrier = "Spectrum Mobile"
term = 6

# Calculate plan cost and total amount paid
plan_calculator(plan_cost, device_payment, device_promo, sales_tax, carrier, term)
```

## Benefits
- **Cost Comparison**: `carrierEstimator` enables you to compare the costs of different phone plans effortlessly. By providing the necessary input parameters, you can quickly see the estimated monthly costs and total amount paid over a specified term for each plan.
- **Customization**: The tool allows you to customize the calculations based on your specific situation. You can input plan costs, device payments, device promotions, and sales tax rates to match the offerings of various carriers.
- **Time and Money Savings**: By automating the comparison process, `carrierEstimator` saves you time and helps you make informed decisions. It provides cost transparency, allowing you to identify the most cost-effective plan that meets your needs while minimizing your expenses.

## Contributing
Contributions to `carrierEstimator` are welcome! If you have suggestions for improvements, encounter any issues, or would like to add new features, please feel free to open an issue or submit a pull request. Your contributions help make `carrierEstimator` better for everyone.

## License
The `carrierEstimator` tool is released under the [GPL-3.0 License](LICENSE). You are free to use, modify, and distribute the code in accordance with the terms of the license.