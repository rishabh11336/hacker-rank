import math
from cmath import phase
C = eval(input())
print(abs(complex(C.real, C.imag)))



print(phase(complex(C.real, C.imag)))