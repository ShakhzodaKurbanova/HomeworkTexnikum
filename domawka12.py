## Урок 1 ##

# Знакомство
print('Ура, мы познакомились!')

## Урок 2 ##

# Переменные
pr = 'Вот так создаются переменные'
# Условные операторы
if pr == 'Это переменная':
    pass
elif pr == 'Вот так создаются переменные':
    print(pr)
else:
    print('А это крайний выбор')

## Урок 3 ##

# Списки
spisok = ['вот', 'как', 'создать', 'spisok', 3]
# Кортежи
kortej = ('a', 'vot', 'eto', 'kortej', 'on', 'ne', 'menyaetsya')

## Урок 4 ##

# Цикл for
n = int(input())
for i in range(1, n + 1):
    print(i ** 2)   # Напечатает квадраты
# Цикл while
n = 10000000
while n > 100:
    print(n)
    n //= 10

## Урок 5 ##

# Форматирование строк
vot = 'форматирование строк'
print(f'Вот это называется {vot}')
# List comprehention
nat_chisla = [i for i in range(1, 101)]
print(nat_chisla)

## Урок 6 ##

# Словари
slovar = {'klyuch':'znacheniye'} # вот так делаются словари
# Сеты
nums = (1,2,2,3,4,5,6,6,7,8,8)
numset = set(nums)
print(numset)    #Сеты почти тоже самое что и список, только без повторений

## Урок 7 ##
# Функции
def function():     # это самая обычная функция
    print('Chto to')

function()   # призыв


## Урок 8 ##
# Анонимная функция
double = lambda x: x * 2
result = double(5)
print(result)


## Урок 9 ##
# Классы
class Cat:
    def meow(self):
        print("Мяу!")

mycat = Cat()
mycat.meow()

## Урок 10 ##
#ООП
class Dog:
  # Представляет собаку с именем и породой

  def __init__(self, name, breed):
    # Инициализирует объект Dog
    self.name = name
    self.breed = breed

  def bark(self):
    # Заставляет собаку лаять
    print(f"{self.name} гавкает: Гав-гав!")

# Создание объектов класса Dog
my_dog = Dog("Рекс", "Овчарка")
your_dog = Dog("Белка", "Йоркширский терьер")

# Вызов метода bark() для каждого объекта
my_dog.bark() # Вывод: Рекс гавкает: Гав-гав!
your_dog.bark() # Вывод: Белка гавкает: Гав-гав!


