# main_script.py
import os

# Запись в файл
with open("example.txt", "w") as file:
    file.write("Hello, this is some text.\n")

# Чтение из файла и вывод на экран
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)

# Добавление строк в файл
with open("example.txt", "a") as file:
    file.write("Additional line 1.\n")
    file.write("Additional line 2.\n")

# Проверка существования файла
if os.path.exists("example.txt"):
    print("File 'example.txt' exists.")
else:
    print("File 'example.txt' does not exist.")
