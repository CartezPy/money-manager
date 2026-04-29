# Money Manager CLI (simple version)

# input data
money = int(input("Enter your money: "))
salary = int(input("Enter your salary: "))
expenses = int(input("Enter your expenses: "))
days = int(input("Enter days: "))

# calculations
total_money = money + salary - expenses
money_per_day = total_money // days
rest_money = total_money % days

# output
print("\n==== RESULT ====")
print(f"Total money: {total_money}")
print(f"Money per day: {money_per_day}")
print(f"Left: {rest_money}")

# check
if days == 0:
    print("Error: days cannot be zero")
    exit()
