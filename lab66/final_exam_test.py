#
# 1. Каква ще бъде стойността на x след като приключи програмата? (5 точки)
# x = 0
# a = 5
# b = 5
# if a>0:
#     if b < 0:
#         x = x + 5
#     elif a > 5:
#         x = x + 4
#     else:
#         x = x + 3
# else:
#     x = x + 2
# print(x)
#
# А) 0
# Б) 4
# В) 2
# Г) 3
#
# ВЕРЕН ОТГОВОР
#
# 2.  Какъв ще бъде изходът от следния фрагмент код? (5 точки)
# myList = [1, 3, 3, 3, 3, 1]
# max = myList[0]
# indexOfMax = 0
# for x in range(1, len(myList)):
#     if myList[x] >= max:
#         max = myList[x]
#         indexOfMax = x # 1

# print(indexOfMax)
#
# А) 0
# Б) 1
# В) 2
# Г) 3
# Д) 4
#
# ВЕРЕН ОТГОВОР
#
# 3. Даден е следният код. Кой ред от номерираните ще хвърли грешка? (5 точки)
# import datetime

# tday = datetime.date.today()
# bday = datetime.date(2020, 9, 18)
# t_day = bday-tday

# print(t_day.months)             # 1
# print(t_day.seconds)            # 2
# print(t_day.max)                # 3
# print(t_day.resolution)         # 4
#
# А) 1
# Б) 2
# В) 3
# Г) 4
#
# ВЕРЕН ОТГОВОР
#
# 4. Кое от следните е метод за четене на файлове? (2 точки)
# А) append
# Б) read
# В) replace
# Г) write
#
# ВЕРЕН ОТГОВОР
#
# 5. Кой е верният синтаксис за инстанциране на нов обект от класът Game? (2 точки)
#    A) my_game = class.Game()
#    Б) my_game = class(Game)
#    В) my_game = Game()
#    Г) my_game = Game.create()
#
# ВЕРЕН ОТГОВОР
#
# 6. Ако една функция не връща стойност какво се случва? (2 точки)
#    А) Функцията ще върне RuntimeError, ако не връща стойност
#    Б) Ако ключовата дума return липсва, функцията ще върне None
#    В) Ако ключовата дума return липсва, функцията ще върне True
#    Г) Функцията ще влезе в безкраен цикъл, защото няма да знае кога да спре   изпълнението на кода
#
# ВЕРЕН ОТГОВОР
#
# 7. Какъв е терминът използван за да опише това което се подава на дадена функция? (2 точки)
#    А) аргументи
#    Б) парадигми
#    В) атрибути
#    Г) декоратори
#
# ВЕРЕН ОТГОВОР
#
# 8. В коя тип колекция се използват ключове да се асоциират стойностите? (2 точки)
#    А) слот
#    Б) речник
#    В) опашка
#    Г) подреден списък
#
# ВЕРЕН ОТГОВОР
#
# 9. Каква е ползата от pass изразът в Python? (2 точки)
#   A) Използва се да прескочи yield изразът на генератор и да върне стойност None.
#   Б) Използва се като null стойност в функции, класове и т.н.
#   В) Използва се за прескачане от един блок към друг.
#   Г) Използва се да прекъсне останалата част от while или for loop цикъл и да се върне в началото на цикъла.
#
# ВЕРЕН ОТГОВОР
#
# 10. Какъв ще бъде изходът от програмата? (5 точки)
# class A:
#     def __init__(self):
#         self.calcI(30)
#         print("i from A is", self.i)

#     def calcI(self, i):
#         self.i = 2 * i

# class B(A):
#     def __init__(self):
#         super().__init__()

#     def calcI(self, i):
#         self.i = 3 * i;

# b = B()
#
# А) init метода на клас А изписва “i from A is 0”.
# Б) init метода на клас A изписва “i from A is 90”.
# В) __init__ метода само на клас B ще се извика.
# Г) init метода на клас A изписва “i from A is 60”
#
# ВЕРЕН ОТГОВОР
#
# 11. Кога цикълът for спира да итерира? (2 точки)
# A) когато срещне безкраен цикъл
# Б) когато срещне блок if/else, което съдържа в себе си break
# В) когато е обходил всеки един елемент от колекцията или е намерена ключова дума break за прекъсване
# Г) когато времето за изпълнение на цикъла надвишава O(n^2)
#
# ВЕРЕН ОТГОВОР
#
# 12. Като се имат предвид следните три списъка, как бихте създали нов списък,
# който съответства на желания изход, отпечатан по-долу? (5 точки)
# fruits = ['Apples', 'Orange', 'Bananas']
# quantities = [5, 3, 4]
# prices = [1.50, 2.25, 0.89]

# # Очакван изход
# [('Apples', 5, 1.50),
# ('Oranges', 3, 2.25),
# ('Bananas', 4, 0.89)]
#
# А)
# output = []


# fruit_tuple_0 = (first[0], quantities[0], price[0])
# output.append(fruit_tuple)

# fruit_tuple_1 = (first[1], quantities[1], price[1])
# output.append(fruit_tuple)

# fruit_tuple_2 = (first[2], quantities[2], price[2])
# output.append(fruit_tuple)

# print(output)
#
# Б)	i = 0
# output = []
# for fruit in fruits:
#     temp_qty = quantities[i]
#     temp_price = prices[i]
#     output.append((fruit, temp_qty, temp_price))
#     i += 1
# return output
#
# В) 	groceries = zip(fruits, quantities, prices)
# return groceries
#
# >>> [
# ('Apples', 5, 1.50),
# ('Oranges', 3, 2.25),
# ('Bananas', 4, 0.89)
# ]
#
# Г) 	i = 0
# output = []
# for fruit in fruits:
#     for qty in quantities:
#         for price in prices:
#             output.append((fruit, qty, price))
#     i += 1
# return output
#
# ВЕРЕН ОТГОВОР
#
# 13. Каква е разликата между set и list? (2 точки)
#  A) Set е подредена колекция от уникални елементи. List е неподредена колекция от неуникални елементи
#  Б) Елементите могат да се върнат от list, не и от set.
#  В) Set е подредена колекция от неуникални елементи. А list е неподредена колекция от уникални елементи.
#  Г) Set е неподредена колекция от уникални елементи. List е подредена колекция от не уникални елементи.
#
# ВЕРЕН ОТГОВОР
#
# 14. Какво ще принтира функцията? (5 точки)
# def print_alpha_nums(abc_list, num_list):
#     for char in abc_list:
#         for num in num_list:
#             print(char, num)
#     return

# print_alpha_nums(['a', 'b', 'c'], [1, 2, 3])

#  A)
# a 1
# a 2
# a 3
# b 1
# b 2
# b 3
# c 1
# c 2
# c 3
#
#  Б) ['a', 'b', 'c'], [1, 2, 3]
#
#  В)
#        aaa
# bbb
# ccc
# 111
# 222
# 333
#
#  Г)
#        a 1 2 3
# b 1 2 3
# c 1 2 3
#
# ВЕРЕН ОТГОВОР
#
# 15. Кой е правилният синтаксис за извикване на  метод от класът наименуван като Game? (2 точки)
# А) my_game = Game()
#    my_game.roll_dice()

# Б) my_game = Game()
#    self.my_game.roll_dice()

# В) my_game = Game(self)
#    self.my_game.roll_dice()

# Г) my_game = Game(self)
#    my_game.roll_dice(self)

# ВЕРЕН ОТГОВОР

# 16. Прегледайте кода по-долу. Какъв е правилният синтаксис за промяна на цената на 1.5? (2 точки)
# fruit_info = { 'fruit': 'apple', 'count': 2, 'price': 3.5 }
# A) fruit_info['price'] = 1.5
# B) my_list[3.5] = 1.5
# C) 1.5 = fruit_info['price']
# D) my_list['price'] == 1.5
# #
# ВЕРЕН ОТГОВОР
#
# 17.  Какъв е правилният начин да се дефинира функция? (2 точки)
# A) def getMaxNum(list_of_nums): # тяло на функцията
# Б) func get_max_num(list_of_nums): # тяло на функцията
# В) func getMaxNum(list_of_nums): # тяло на функцията
# Г) def get_max_num(list_of_nums): # тяло на функцията

# ВЕРЕН ОТГОВОР
#
# 18. Кое твърдение е вярно за клас методите? (2 точки)
# A) Клас методът държи всички данни за даден клас
# Б) Клас методът може да модифицира състоянието на класа,
# но не може директно да модифицира състоянието на инстанцията, която наследява от този клас.
# В) Клас методът е обикновена функция която принадлежи на клас, но трябва да връща стойност None
# Г) Клас методът е подобен на обикновена функция, но клас метода не приема никакви аргументи.
#
# ВЕРЕН ОТГОВОР
#
# 19. Кога бихте използвали цикъл for? (2 точки)
# A) Само в някои ситуации, тъй като циклите се използват само за определен тип програмиране
# Б) Когато трябва да проверите всеки елемент в колекция с известна дължина
# В) Когато искате да минимизирате използването на стрингове във вашият код
# Г) Когато искате да стартирате код в един файл за функция в друг файл
#
# ВЕРЕН ОТГОВОР
#
# 20. Мениджмънта е пуснал запитване за създаване на база от данни за служители.
# Вие сте започнали с таблицата за служители. Кой е верният синтаксис? (5 точки)
#
# А)  1 CREATE TABLE employee (
#     2 employee ID char(10),
#     3 firstName varchar(50),
#     4 lastName varchar(50),
#     5 phone varchar(20),
#     6 address varchar(50),
#     7 PRIMARY KEY ON employeeID
#     8 );
#
# Б)  1 CREATE TABLE employee (
#     2 employee ID char(10),
#     3 firstName varchar(50),
#     4 lastName varchar(50),
#     5 phone varchar(20),
#     6 address varchar(50),
#     7 PRIMARY KEY employeeID
#     8 );
#
# В)  1 CREATE TABLE IF EXISTS employee (
#     2 employee ID char(10),
#     3 firstName varchar(50),
#     4 lastName varchar(50),
#     5 phone varchar(20),
#     6 address varchar(50),
#     7 PRIMARY KEY (employeeID)
#     8 );
#
#
#
# Г)  1 CREATE TABLE IF NOT EXISTS employee (
#     2 employee ID char(10),
#     3 firstName varchar(50),
#     4 lastName varchar(50),
#     5 phone varchar(20),
#     6 address varchar(50),
#     7 PRIMARY KEY (employeeID)
#     8 );
#
# ВЕРЕН ОТГОВОР
#
# 21. За какво се използва функцията strip? (2 точки)
#
# А) Изтрива съдържанието на целия файл
# Б) Премахва допълнителни данни от началото/края на стринга
# В) Разделя файл на две части
# Г) Добавя метаданни
#
# ВЕРЕН ОТГОВОР
#
# 22. Кой е верният синтаксис за добавяне на данни към таблица? (2 точки)
# А) insert into cars (make, model, year) values ('Ford', 'Mustang', 2002) ('Mercedes', 'C', 2003)
#
# Б) insert into cars (make, model, year) values ('Ford', 'Mustang', 2002) values ('Mercedes', 'C', 2003)
#
# В) insert into cars (make, model, year) extended ('Ford', 'Mustang', 2002), ('Mercedes', 'C', 2003)
# Г) insert into cars (make, model, year) values ('Ford', 'Mustang', 2002), ('Mercedes', 'C', 2003)
#
# ВЕРЕН ОТГОВОР
#
# 23. Коя заявка ще покаже всички граждани на възраст повече от 21 години? (2 точки)
# А) db.citizens.select('WHERE age >= 21')
# Б) db.citizens.select('age >= 21')
# В) db.citizens.select('WHERE age >= 21')
# Г) db.citizens.select({age: {$gte: 21}})
#
# ВЕРЕН ОТГОВОР
#
# 24. Какво съдържа MongoDB? (2 точки)
# А) data
# Б) documents
# В) fields
# Г) rows
#
# ВЕРЕН ОТГОВОР
#
# 25. Какъв е типа на данните прочетен от файл? (2 точки)
# А) Integer
# Б) Boolean
# В) String
# Г) Real
#
# ВЕРЕН ОТГОВОР
#
# 26. Как се създава текстов индекс? (2 точки)
# А) db.customers.createIndex({firstName, lastName})
# Б) db.customers.createTextIndex({firstName, lastName})
# В) db.customers.createIndex({firstName: "text", lastName: "text"})
# Г) db.customers.createText({firstName: 1, lastName: 1})
#
# ВЕРЕН ОТГОВОР
#
# 27. Искате набор от документи да бъдат върнати с фамилно име във възходящ ред. Коя заявка ще постигне това? (2 точки)
# А) db.persons.find().sort({lastName: -1}}
# Б) db.persons.find().sort({lastName: 1}}
# В) db.persons.find().sort({lastName: ascending}}
# Г) db.persons.find().sort({lastName: $asc}}
#
# ВЕРЕН ОТГОВОР
#
# 28. Какво се случва в кода по-долу? (5 точки)
class A:
    def __init__(self, i=100):
        self.i = i

class B(A):
    def __init__(self, j=0):
        self.j = j
def main():
    b = B()
    print(b.i)
    print(b.j)

main()

# А) Клас B наследява всички полета от клас А.
# Б) Клас B се нуждае от аргумент.
# В) Член променливата j не може да бъде да се достъпи от обект b.
# Г) Клас B наследява клас A, но член променливата i в A не може да бъде наследена.
#
# ВЕРЕН ОТГОВОР
#
# 29. Какъв ще бъде изходът от следният код? (5 точки)
# def total(initial=5, *num, **key):
#     count = initial
#     for n in num:
#         count += n
#     for k in key:
#         count += key[k]
#     return count
# print(total(100, 2, 3, clouds=50, stars=100))
#
# А) 260
# Б) 160
# В) 155
# Г) 255
#
# ВЕРЕН ОТГОВОР
#
# 30. Попълнете празното така, че кодът да генерира графиките по-долу. (5 точки)
# import matplotlib.pyplot as plt
# sample_figure = plt.figure()
# ax1 = _______________________
# ax2 = _______________________
# ax1.hist(data)
# ax2.boxplot(data)
# plt.show()
#
#
# А) 1- ax.add_subplot(122) 2 – ax.add_subplot(121)
# Б) 1- sample_figure.add_subplot(121) 2- sample_figure.add_subplot(122)
# В) 1- add_subplot(121) 2- add_subplot(122)
# Г) 1- sample_figure.add(1,2,2) 2- sample_figure(1,2,1)
#
# ОТГОВОР НЯМАМ
#
# 31. Имате следният код: (5 точки)
# def test_scores(total_questions=0, total_correct=0):
#     return int(total_correct) / int(total_questions)
#
#       Кое от изброените по-долу ще хвърли Runtime error?
# А) test_score = test_scores(20, 19)
# Б) test_score = test_scores(“20”, “19”)
# В) test_score = test_scores(1)
# Г) test_score = test_scores(0, 20)
# Д) Нито едно от изброените
#
# ВЕРЕН ОТГОВОР
#
# 32. Имате следният код: (5 точки)
#       def calc1(rate, item):
#     	item *= (1 + rate)
#
#       rate = 0.25
#       item = 12000
#
#       calc1(rate, item)
#       print('Rate: ', rate, '; Value: ', item)
#
#       Какво ще се отпечата на екрана?
#       А) Rate: 0.25 ; Value: 12000
#       Б) Rate: 0.25 ; Value: 15000
#       В) Rate: 1.25 ; Value: 15000
#       Г) Rate: 1.25 ; Value: 12000
#
# ВЕРЕН ОТГОВОР
#
