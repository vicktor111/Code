def exam_code(code: str):
    result = 0
    if len(code) == 13: # Перевірка чи це 13 річний штрих код
        sum_1 = 0
        sum_2 = 0
        control_num = int(code[len(code) - 1]) # Беремо контрольне число
        print("Іде перевірка/"+ str(control_num))
        for i in range(len(code) - 1):
            if i % 2:
                sum_1 += int(code[i]) # Сумуємо всі числа на парних місцях штрих коду
                code_1 += code[i]
            else:
                sum_2 += int(code[i]) # Сумуємо всі числа на непарних місцях штрих коду
                code_2 += code[i]
        sum_1 = sum_1 * 3 # Множемо першу суму на 3
        result = sum_1 + sum_2 # Додаємо ці суми
        result = int(str(result)[len(str(result)) - 1]) # Дістаємо останю цифру з числа
        result = 10 - result
        return control_num == result # перевірка чи це правильний штрих код.
