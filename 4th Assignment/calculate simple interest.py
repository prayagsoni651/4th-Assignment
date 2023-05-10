# 8. Write a python script to calculate simple interest


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))

interest = (principal * rate * time) / 100

print(f"The simple interest for principal {principal}, rate of interest {rate}% and time period {time} years is {interest}")
