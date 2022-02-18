# создание обычной строки
s = 'Hello world!'
# тип обычной строки
print(type(s))

# создание строки байт
sb = b'Hello world!'
# тип строки байт
print(type(sb))
# вывод строки байт
print(sb)

# индекс в обычной строке
print(s[1])
# индекс в строке байт
print(sb[1])

# срез в обычной строке
# print(s[1:3])
# # срез в строке байт
# print(sb[1:3])
# # перебор строки байт в цикле
# for item in sb:
#     print(item)

# кодирование строки в определенную кодировку
ss = 'Hello world Мир'
ssb = ss.encode('utf-8')
print(ssb)
print(type(ssb))

# декодирование строки
ss = ssb.decode('utf-8')
print(ss)
print(type(ss))