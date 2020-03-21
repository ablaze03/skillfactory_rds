import numpy as np
import random
count = 0      # счетчик попыток
number = random.randint(1,100)    # загаданное число
max_level = 99 # верхняя граница
min_level = 1  # нижняя граница
predicat = round((min_level+max_level)/2)  # предсказание
while True: # бесконечный цикл
    count+=1 # cчитаем количество попыток угадывания
    if predicat == number: # если число угадано
        print(f"Число {number} угадано за {count} попыток")        # выводим на экран количество попыток
        break              #завершаем 
    elif predicat < number: # eсли предсказание меньше числа
        min_level = predicat # нижняя граница равна предсказанию
        predicat = round((max_level + predicat)/2) # новое предсказание 
        
    else: # если предсказание больше числа
        max_level = predicat # верхняя граница равна предскаханию
        predicat = round((min_level + predicat)/2) # новое предсказание
