# Assume you want an output of
####
####
####
####
for j in range(4):
    for i in range(4):
        print(" # ", end="")
    print()

# for i in range(4):
#     print(" # ", end="")
# print()  # Suggests print a new line
#
# for i in range(4):
#     print(" # ", end="")
# print()
#
# for i in range(4):
#     print(" # ", end="")


# To get the output as
#
##
###
####
for j in range(4):
    for i in range(j + 1):
        print(" # ", end="")
    print()
    print()

# Getting output as
####
###
##
#

for j in range(4):
    for i in range(4 - j):
        print(" # ", end="")
    print()
