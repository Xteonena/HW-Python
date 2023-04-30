class FileOperations:
    @staticmethod
    def create_file():
        try:
            filename = input("Enter the file name: ")
            with open(filename, 'w') as file:
                pass
        except Exception:
            print("The name is unacceptable")

    @staticmethod
    def create_star_file(file_name):
        n = int(input("Enter N: "))
        k = int(input("Enter K: "))
        with open(file_name, 'w') as file:
            for _ in range(n):
                file.write('*' * k + '\n')

    @staticmethod
    def remove_first_line(file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()

        with open(file_name, 'w') as file:
            file.writelines(lines[1:])

    @staticmethod
    def remove_k_chars(file_name, k):
        with open(file_name, 'r') as file:
            lines = file.readlines()

        with open(file_name, 'w') as file:
            for line in lines:
                file.write(line[k:])


if __name__ == '__main__':
    file_operations = FileOperations()

    while True:
        print("Select a task:")
        print("1. Create file")
        print("2. Create a text file with N lines, consisting of K characters '*'")
        print("3. Delete the first line of the file")
        print("4. Delete K characters from each line of the file")
        print("0. Exit")
        choice = int(input("Enter task number: "))

        if choice == 1:
            file_operations.create_file()
        elif choice == 2:
            file_name = input("Enter the file name: ")
            file_operations.create_star_file(file_name)
        elif choice == 3:
            file_name = input("Enter file name: ")
            file_operations.remove_first_line(file_name)
        elif choice == 4:
            file_name = input("Enter filename: ")
            k = int(input("Enter K: "))
            file_operations.remove_k_chars(file_name, k)
        elif choice == 0:
            break
        else:
            print("Wrong task number. Try again.")
