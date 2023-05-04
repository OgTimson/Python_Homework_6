# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их 
# в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники. Для каждого 
# холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" 
# (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести 
# номер холодильника, нумерация начинается с единицы.
# Формат входных данных:
# В первой строке подаётся число n – количество холодильников. В последующих n строках вводятся строки, содержащие 
# латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.
# Формат выходных данных:
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего 
# выводить не нужно.
# Sample Input 1: 6         Sample Output 1: 1 2 3
# 1: 222anton456
# 2: a1n1t1o1n1
# 3: 0000a0000n00t00000o000000n
# 4: gylfole
# 5: richard
# 6: ant0n
# Sample Input 2: 9         Sample Output 2: 1 2 7 8
# 1: osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# 2: anton
# 3: aoooooooooontooooo
# 4: elelelelelelelelelel
# 5: ntoneeee
# 6: tonee
# 7: 253235235a5323352n25235352t253523523235oo235523523523n
# 8: antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# 9: unton

from re import match

n = int(input('Введите количество холодильников: '))
print(f'\nНиже введите строки с данными для {n} холодильников:')
strings = [str(input()) for i in range(n)]
key = '.*a.*n.*t.*o.*n.*' # паттерн регулярных выражений для поиска последовательности 'anton'
print('\nНомера зараженных холодильников:', end=' ')
res = [print(i+1, end=' ') for i in range(n) if match(key, strings[i])]
if not res:
    print('Зараженных холодильников нет')