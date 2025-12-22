import re
from typing import Callable





def generator_numbers(text: str) -> float:
    '''
    Функція-генератор аналізує текст та ідентифікує всі дійсні числа в строці 
    та повертає числа, що відповідає критеріям генерування.
    (Чи правильно в мене стоїть тип повернення? Бо pylance у vscode підкреслює мені float.
    Чи правильний тип повернення для генератору?)
    '''
    # додаємо у список усі сходження в тексті за паттерном 'ЧИСЛАкрапкаЧИСЛА'
    numbers = re.findall(r'\d+\.\d+' , text) 
    # ітеруємося по списку та повертаємо число зі списку, заморожуючи стан до наступного виклику
    for number in numbers:
        yield float(number)


def sum_profit(text: str, func: Callable[[str], float]) -> float:
    '''
    Функція, що приймає на вхід строку та функцію-генератор та
    повертає float сумму чисел з генератора.
    '''
    return sum(func(text))










def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    gen = generator_numbers(text)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")









if __name__ == '__main__':
    main()