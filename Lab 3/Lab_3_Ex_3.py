class Coputation:
    def __init__(self):
        pass

    def factorial(self, x):
        if x < 0:
            raise ValueError("n must be a non-negative integer")
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

    def sum(self, x):
        if x < 1:
            raise ValueError("n must be a positive integer")
        result = 0
        for i in range(1, x + 1):
            result += i
        return result

    def test_prim(self, x):
        if x <= 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    def test_prims(self, x1, x2):
        return self.test_prim(x1) and self.test_prim(x2)

    def table_mult(self, x):
        for i in range(1, 11):
            print(f"{x} x {i} = {x * i}")

    def all_tables_mult(self):
        for i in range(1, 10):
            print(f"\nMultiplication table for {i}:")
            self.table_mult(i)

    @staticmethod
    def list_div(x):
        if x < 1:
            raise ValueError("n must be a positive integer")
        ldiv = []
        for i in range(1, int(x ** 0.5) + 1):
            if x % i == 0:
                ldiv.append(i)
                if i != x // i:
                    ldiv.append(x // i)
        return ldiv

    @staticmethod
    def list_div_prim(x):
        if x < 1:
            raise ValueError("n must be a positive integer")
        ldiv = []
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                if Coputation().test_prim(i):
                    ldiv.append(i)
                if Coputation().test_prim(x // i):
                    ldiv.append(x // i)
        return ldiv

# A new instance of the Coputation class is created and assigned to the calculation variable
calculation = Coputation()

# A while loop is used to keep the program running until the user chooses to exit
while True:
    choice = input("""What method do you want to run? 
    1. Factorial
    2. Sum
    3. Test prim
    4. Test prims
    5. Table multiplication
    6. All tables multiplication
    7. List divisors
    8. List prime divisors
    9. Exit
    Enter your choice: """)

# Depending on the choice, the appropriate method is called from the calculation object with the necessary arguments
    if choice == "1":
        n = int(input("Enter a number to find its factorial: "))
        print(f"Factorial of {n} is {calculation.factorial(n)}")
    elif choice == "2":
        n = int(input("Enter a number to find the sum of first n integers: "))
        print(f"Sum of first {n} integers is {calculation.sum(n)}")
    elif choice == "3":
        n = int(input("Enter a number to test if it's prime: "))
        if calculation.test_prim(n):
            print(f"{n} is a prime number")
        else:
            print(f"{n} is not a prime number")
    elif choice == "4":
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        if calculation.test_prims(n1, n2):
            print(f"{n1} and {n2} are both prime numbers")
        else:
            print(f"At least one of {n1} and {n2} is not a prime number")
    elif choice == "5":
        n = int(input("Enter a number to generate its multiplication table: "))
        calculation.table_mult(n)
    elif choice == "6":
        calculation.all_tables_mult()
    elif choice == "7":
        n = int(input("Enter a number to list its divisors: "))
        print(f"Divisors of {n} are {calculation.list_div(n)}")
    elif choice == "8":
        n = int(input("Enter a number to list its prime divisors: "))
        print(f"Prime divisors of {n} are {calculation.list_div_prim(n)}")
    elif choice == "9":
        break
    else:
        print("Invalid choice. Try again.")
