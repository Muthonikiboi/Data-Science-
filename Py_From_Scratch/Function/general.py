def greet():
    print("My first Python Function")


greet()


def get_totals(exp):
    total = 0
    for i in exp:
        total = total + i
    return total


salaries = [27000, 12456, 87000, 75000, 90876]

total_salary = get_totals(salaries)
print("The total of the salaries is:", total_salary)
