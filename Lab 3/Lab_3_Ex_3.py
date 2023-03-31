class Computation:
    """
    A class containing methods for various mathematical computations.
    """

    def __init__(self):
        pass

    @staticmethod
    def factorial(x: int) -> int:
        """
        Computes the factorial of a non-negative integer x.
        Args:
            x (int): a non-negative integer
        Returns:
            int: the factorial of x
        Raises:
            ValueError: if x is negative
        """
        if x < 0:
            raise ValueError("x must be a non-negative integer")
        results = 1
        for i in range(1, x + 1):
            results *= i
        return results

    @staticmethod
    def sum(x: int) -> int:
        """
        Computes the sum of the first x positive integers.
        Args:
            x (int): a positive integer
        Returns:
            int: the sum of the first x positive integers
        Raises:
            ValueError: if x is not positive
        """
        if x < 1:
            raise ValueError("x must be a positive integer")
        results = 0
        for i in range(1, x + 1):
            results += i
        return results

    @staticmethod
    def test_prim(x: int) -> bool:
        """
        Determines whether a given integer x is prime.
        Args:
            x (int): an integer to test for primality
        Returns:
            bool: True if x is prime, False otherwise
        """
        if x <= 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    def test_prims(self, x1: int, x2: int) -> bool:
        return self.test_prim(x1) and self.test_prim(x2)

    @staticmethod
    def table_mult(x: int) -> str:
        """
        Generates a multiplication table for a given integer x.
        Args:
            x (int): the integer for which to generate a multiplication table
        Yields:
            str: a string representing one row of the multiplication table
        """
        for i in range(1, 11):
            yield f"{x} x {i} = {x * i}"

    @property
    def all_tables_mult(self) -> str:
        """
        Generates multiplication tables for the numbers 1 through 9.
        Returns:
            str: a string containing all the multiplication tables
        """
        tables = []
        for i in range(1, 10):
            table = list(self.table_mult(i))
            tables.append(f"\nMultiplication table for {i}:\n" + '\n'.join(table))
        return '\n'.join(tables)

    @staticmethod
    def list_div(x: int) -> list[int]:
        """
        Lists the divisors of a given integer x.
        Args:
            x (int): the integer for which to list the divisors
        Returns:
            list: a list of the divisors of x
        Raises:
            ValueError: if x is not positive
        """
        if x < 1:
            raise ValueError("x must be a positive integer")
        ldiv = []
        for i in range(1, int(x ** 0.5) + 1):
            if x % i == 0:
                ldiv.append(i)
                if i != x // i:
                    ldiv.append(x // i)
        return ldiv

    @staticmethod
    def list_div_prim(x: int) -> list[int]:
        """
        Returns a list of all prime divisors of x.

        Args:
            x (int): A positive integer to find prime divisors for.

        Returns:
            list: A list of all prime divisors of x.

        Raises:
            ValueError: If x is less than 1.
        """
        if x < 1:
            raise ValueError("x must be a positive integer")
        ldiv = []
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                if Computation().test_prim(i):
                    ldiv.append(i)
                if Computation().test_prim(x // i):
                    ldiv.append(x // i)
        return ldiv


# A new instance of the Computation class is created and assigned to the calculation variable
calculation = Computation()

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
        for result in calculation.table_mult(n):
            print(result)
    elif choice == "6":
        result = calculation.all_tables_mult
        print(result)
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
