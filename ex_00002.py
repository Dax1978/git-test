# откерываем файл для записи байтов
with open('bytes.txt', 'wb') as f:
    # пишем строку байт
    f.write(b'Hello bytes')

# with open('bytes.txt', 'rb') as f:
#     pass
#
# # открываем файл в текстовом режиме с указанием кодировки
# with open('bytes.txt', 'r', encoding='utf-8') as f:
#     pass

# читаем как текст
with open('bytes.txt', 'r', encoding='ascii') as f:
    print(f.read())

# откерываем файл для записи байтов
with open('bytes.txt', 'wb') as f:
    # пишем строку байт
    str = 'Привет мир'
    f.write(str.encode('utf-8'))

# читаем как текст с кодировкой utf-8
with open('bytes.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# открываем файл в режиме чтения байтов
with open('bytes.txt', 'rb') as f:
    # читаем байты
    result = f.read()
    print(result)
    print(type(result))
    # декодируем для получения строки
    s = result.decode('utf-8')
    print(s)