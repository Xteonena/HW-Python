# Создаём функцию
def pair(i): # Задаём переменную i
    if i % 2 == 0: # Проверяем делиться ли i на 2
        return True # Возвращаем True, если i делится на 2
    else:
        return False # Возвращаем False, если i не делится на 2

x = int(input("Введите число: ")) # Ввод произвольного числа

# Проверка на парность
if pair(x): # Вызываем функцию pair и присваиваем ей переменную x
    print(f"{x} это чётное число") # Выводит, если число делится на 2git remote add origin git@github.com:Xteonena/HW-for-Python-course.git
else:
    print(f"{x} это нечётно число") # Выводит, если число не делится на 2