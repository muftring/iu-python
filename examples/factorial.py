# factorial.py
#    Program to compute the factorial of a number
#    Illustrates for loop with an accumulator
def main():
    n = eval(input("Please enter a number: "))
    fact = 1
    for j in range(n,1,-1):
       fact = fact * j
    print("The factorial of", n, "is", fact)
    
main()
