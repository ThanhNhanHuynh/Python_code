a = int(input("Enter a: "))
b = int(input("Enter b: "))

def user_input():
    print("1st number: a =",a)
    print("2nd number: b =",b)

def calculation():
    print("Sum =",int(a + b))
    print("Difference =",int(a - b))
    print("Product =",int(a * b))
    print("Quotient =",int(a / b))

user_input()
calculation()