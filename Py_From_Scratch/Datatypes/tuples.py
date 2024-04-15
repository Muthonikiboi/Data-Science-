#  This involves putting information inside the brackets()
#  We cannot change change a tuple delete or even add values
from typing import Tuple

car = ("BMW", "Mazda CX5", "Mazda Demio", "Mazda Axela")
print(car)

#  Tuple does not support item assignment
car[3] = "Vitz"

print(car)
