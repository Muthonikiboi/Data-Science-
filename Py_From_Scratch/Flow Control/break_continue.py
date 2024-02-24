# break-exits the loop at the stated point
# continue assumes the if condition and continues to the next iteration-->example it skips 2

for i in range(50):
    if i == 33:
        # Break exits the piece of code where i is 33
        break
    print(i)

for x in range(5):
    if x == 2:
        continue
    print(x)


