# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

sum = int(input("Введите сумму загаданных чисел : "))
pow = int(input("Введите произведение загаданных чисел : "))
for i in range(sum):
    for j in range(pow):
        if sum == i + j and pow == i * j:
            print("Ваши числа: ")
            print(i, j)
            