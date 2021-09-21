# Сумма всех цифр в числе
flag = "Д"
while flag == "Д":
    summa = 0
    digit = input("Введите число: ")
    for i in range(len(digit)):
        if digit[i] in "1234567890":
            summa += int(digit[i])
        else:
            print("Вы ввели неподходящий символ. Попробуйте снова.")
            flag = "н"
    if flag != "н":
        print(summa)
    flag = input("Продолжить? Д/н: ")