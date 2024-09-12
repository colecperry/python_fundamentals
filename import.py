# Observe differences when importing from a library
import math
print(math.sqrt(9))

from math import sqrt #Can lead to name conflicts if you have another variable "sqrt"
print(sqrt(16))

from math import * #Can lead to name conflicts if you have another variable "sqrt"
print(sqrt(25))

# ABSOLUTE IMPORTS - An absolute import specifies the module to be imported using the full path from the root directory

# absolute_package
# ├── package1
# │   ├── module1.py
# │   └── module2.py
# ├── package2
# │   ├── module3.py
# │   ├── module4.py
# │   ├── module5.py
# │   └── subpackage1
# │       └── module6.py

# Let's assume that there is a function called function1() in each module that prints:

# $ python
# >>> from package1 import module1
# >>> module1.function1()
# => Function 1 in module 1

# $ python
# >>> from package1.module1 import function1
# >>> function1()
# # => Function 1 in module 1

# $ python
# >>> from package2.subpackage1.module6 import function1
# >>> function1()
# # => Function 1 in module 6