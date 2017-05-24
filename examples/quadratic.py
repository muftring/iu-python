# quadratic.py
#    Computes the roots of a quadratic equation.
#    Crashes if the equation has no real roots.
import math  # Makes the math library available.
def main():
    print("This program finds the real solutions to a quadratic equation")
    print()
    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    discriminant = math.sqrt(b*b - 4*a*c)
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    print()
    print("The solutions are:", root1, root2 )
main()
