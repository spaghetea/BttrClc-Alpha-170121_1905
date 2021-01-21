# use Colorama to make Termcolor work on Windows too use init()
from colorama import init
from colorama import Fore, Back, Style

init()

print(Back.BLACK)
print(Fore.WHITE)

print("Добро пожаловать в калькулятор alpha_180121_! Были добавлены украшательства и возможность вывода целого числа при делении. Все обновления можно прочитать в документе changelog")

what = input("Операция (+, -, *, /, ** (степень), % (вывод остатка), // (вывод целого числа)): ")

print(Back.BLACK)
print(Fore.WHITE)

a = float( input("Первое число: ") )
b = float( input("Второе число: ") )

print(Back.BLACK)
print(Fore.WHITE)

if what == "+":
    c = a + b
    print("Результат: " + str(c))
elif what == "-":
    c = a - b
    print("Результат: " + str(c))
elif what == "*":
    c = a * b
    print("Результат: " + str(c))
elif what == "/":
    c = a / b
    print("Результат: " + str(c))
elif what == "**":
    d = float( input("Введите степень: ") )
    c = a ** d
    print("Результат: " + str(c))
elif what == "%":
    e = float( input("Введите число по модулю: ") )
    c = a % e
    print("Результат: " + str(c))
elif what == "//":
    c = a // b
    print("Результат: " + str(c))
else:
    print("Неверная операция")

input("Нажмите \"Enter\", чтобы закрыть калькулятор")