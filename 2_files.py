"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('download/referat.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print(len(content))
        print(len(content.split(" ")))
        content = content.replace(".", "!")

    with open('download/referat2.txt', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    main()
