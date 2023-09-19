"""
Electricity Bill Calculator
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
user_tariff = int(input("Which tariff? 11 or 31: "))
daily_kwh_use = float(input("Enter daily use in KWh: "))
billing_period = float(input("Enter number of billing days: "))

if user_tariff == 11:
    electricity_bill = TARIFF_11 * daily_kwh_use * billing_period
    print(f"Estimated bill: ${electricity_bill:.2f}")
elif user_tariff == 31:
    electricity_bill = TARIFF_31 * daily_kwh_use * billing_period
    print(f"Estimated bill: ${electricity_bill:.2f}")
else:
    print("Not a valid tariff")
