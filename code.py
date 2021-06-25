import matplotlib.pyplot as plt
import math

def prime(n):
    if n % 2 == 0:
        return False  # number is not prime
    iterations = int(math.sqrt(n)) + 1
    for i in range(3, iterations, 2):
        if n % i == 0:
            return False
    return True


max_number = 100
for i in range(3, max_number, 1):
    if prime(i):
        if prime(i+2):
            print(str(i), " + " + str(i + 2), " are twin primes", end=" ")
            if (i+1) % 6 == 0:
                print("mid num % 6 is 0")
            else:
                print("mid number % 6 isnt 0")


"""
#  this section is here for later development, in order to display on a graph

x = [10,20,30,40,50] # meaningless numbers, here for testing
y = [1,2,3,4,5]

plt.scatter(x, y, label="", color="green", marker="*", s=30)

plt.ylabel('y label')
plt.xlabel('x label')
plt.title('difference between sequential twin primes')
plt.legend()

plt.show()
"""
